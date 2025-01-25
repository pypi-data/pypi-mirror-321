import zarr
import os
from zarrify.utils.volume import Volume

class N53D(Volume):
    def __init__(
        self,
        src_path: str,
        axes: list[str],
        scale: list[float],
        translation: list[float],
        units: list[str],
    ):
        """Construct all the necessary attributes for the proper conversion of tiff to OME-NGFF Zarr.

        Args:
            input_filepath (str): path to source tiff file.
        """
        super().__init__(src_path, axes, scale, translation, units)
        self.store_path, self.arr_path = self.separate_store_path(src_path, '')
        self.n5_store = zarr.N5Store(self.store_path)
        self.n5_arr = zarr.open(store = self.n5_store, path=self.arr_path, mode='r')

        self.shape = self.n5_arr.shape
        self.dtype = self.n5_arr.dtype
        self.chunks = self.n5_arr.chunks
        
    def separate_store_path(store, path):
        """
        sometimes you can pass a total os path to node, leading to
        an empty('') node.path attribute.
        the correct way is to separate path to container(.n5, .zarr)
        from path to array within a container.

        Args:
            store (string): path to store
            path (string): path array/group (.n5 or .zarr)

        Returns:
            (string, string): returns regularized store and group/array path
        """
        new_store, path_prefix = os.path.split(store)
        if ".n5" in path_prefix:
            return store, path
        return separate_store_path(new_store, os.path.join(path_prefix, path))