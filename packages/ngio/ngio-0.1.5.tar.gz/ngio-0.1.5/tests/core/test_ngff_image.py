from pathlib import Path


class TestNgffImage:
    def test_ngff_image(self, ome_zarr_image_v04_path: Path) -> None:
        from ngio.core.ngff_image import NgffImage

        ngff_image = NgffImage(ome_zarr_image_v04_path)
        image_handler = ngff_image.get_image(path="0")
        ngff_image.__repr__()

        assert ngff_image.num_levels == 5
        assert ngff_image.levels_paths == ["0", "1", "2", "3", "4"]
        assert image_handler.channel_labels == ["DAPI", "nanog", "Lamin B1"]
        assert image_handler.get_channel_idx(label="DAPI") == 0
        assert image_handler.get_channel_idx(wavelength_id="A01_C01") == 0

        new_path = ome_zarr_image_v04_path.parent / "new_ngff_image.zarr"
        new_ngff_image = ngff_image.derive_new_image(
            new_path, "new_image", overwrite=True
        )
        new_image_handler = new_ngff_image.get_image(path="0")

        assert new_ngff_image.levels_paths == ngff_image.levels_paths
        assert new_image_handler.channel_labels == image_handler.channel_labels
        assert new_image_handler.shape == image_handler.shape
        assert new_image_handler.pixel_size.zyx == image_handler.pixel_size.zyx
        assert (
            new_image_handler.on_disk_array.shape == image_handler.on_disk_array.shape
        )
        assert (
            new_image_handler.on_disk_array.chunks == image_handler.on_disk_array.chunks
        )
        new_ngff_image.lazy_init_omero(
            labels=3,
            wavelength_ids=["A01_C01", "A02_C02", "A03_C03"],
            consolidate=True,
        )

        new_ngff_image.update_omero_window(start_percentile=1.1, end_percentile=98.9)

    def test_ngff_image_derive(self, ome_zarr_image_v04_path: Path) -> None:
        from ngio.core.ngff_image import NgffImage

        ngff_image = NgffImage(ome_zarr_image_v04_path)

        for name, table_type in [("test_roi", "roi_table")]:
            table = ngff_image.tables.new(name=name, table_type=table_type)
            table.consolidate()

        ngff_image.labels.derive("test_label")

        new_path = ome_zarr_image_v04_path.parent / "new_ngff_image.zarr"
        new_ngff_image = ngff_image.derive_new_image(
            new_path, "new_image", overwrite=True, copy_labels=True, copy_tables=True
        )

        assert ngff_image.tables.list() == new_ngff_image.tables.list()
        assert ngff_image.labels.list() == new_ngff_image.labels.list()
