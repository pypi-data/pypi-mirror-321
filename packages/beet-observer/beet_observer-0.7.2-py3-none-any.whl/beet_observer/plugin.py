from beet import Context, run_beet

from .data_pack import gen_dp_overlays
from .resource_pack import gen_rp_overlays


def beet_default(ctx: Context):
    if "observer" not in ctx.meta:
        return

    # check cache
    cache = ctx.cache["observer"]
    cached_dp = False
    cached_rp = False
    dp_path = None
    rp_path = None
    if ctx.data:
        dp_path = cache.get_path(f"{ctx.directory} saved_data_pack")
        if dp_path.is_dir():
            ctx.data.load(f"{dp_path}")
            cached_dp = True
    if ctx.assets:
        rp_path = cache.get_path(f"{ctx.directory} saved_resource_pack")
        if rp_path.is_dir():
            ctx.assets.load(f"{rp_path}")
            cached_rp = True
    if cached_dp and cached_rp:
        return

    # get default directories
    if "default_dir" not in ctx.meta["observer"]:
        # default dir not defined
        ctx.meta["observer"]["default_dir_dp"] = "default_overlay"
        ctx.meta["observer"]["default_dir_rp"] = "default_overlay"
    elif isinstance(ctx.meta["observer"]["default_dir"], str):
        # default dir is the same for dp and rp
        ctx.meta["observer"]["default_dir_dp"] = ctx.meta["observer"]["default_dir"]
        ctx.meta["observer"]["default_dir_rp"] = ctx.meta["observer"]["default_dir"]
    else:
        # default dir is different for dp and rp
        ctx.meta["observer"]["default_dir_dp"] = ctx.meta["observer"]["default_dir"][
            "dp"
        ]
        ctx.meta["observer"]["default_dir_rp"] = ctx.meta["observer"]["default_dir"][
            "rp"
        ]
    # save current overlays
    save_dp: list[str] = []
    save_rp: list[str] = []
    for overlay in ctx.data.overlays:
        save_dp.append(overlay)
    for overlay in ctx.assets.overlays:
        save_rp.append(overlay)
    # loop through all overlays
    for overlay in ctx.meta["observer"]["overlays"]:
        # get pack
        if overlay["process"].startswith("https://"):
            load = overlay["process"]
        else:
            load = f"{ctx.directory}/{overlay['process']}"
        # generate context for overlay pack
        with run_beet(
            config={"data_pack": {"load": load}, "resource_pack": {"load": load}}
        ) as ctx_overlay:
            if "directory" not in overlay:
                dp_dir = f"overlay_{ctx_overlay.data.pack_format}"
                rp_dir = f"overlay_{ctx_overlay.assets.pack_format}"
            else:
                dp_dir = overlay["directory"]
                rp_dir = overlay["directory"]
            # compare build pack and overlay pack
            if not cached_dp and ctx.data:
                gen_dp_overlays(ctx, ctx_overlay, dp_dir, save_dp)
            if not cached_rp and ctx.assets:
                gen_rp_overlays(ctx, ctx_overlay, rp_dir, save_rp)

    # save to cache
    if not cached_dp and ctx.data:
        ctx.data.save(path=dp_path)
    if not cached_rp and ctx.assets:
        ctx.assets.save(path=rp_path)
