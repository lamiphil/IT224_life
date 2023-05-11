#include "kernel/ocl/common.cl"


__kernel void rotation90_ocl (__global unsigned *in, __global unsigned *out)
{
  __local unsigned tile[GPU_TILE_W][GPU_TILE_H];

  int x = get_global_id (0);
  int y = get_global_id (1);
  int xloc = get_local_id(0);
  int yloc = get_local_id(1);

  tile[GPU_TILE_W - xloc - 1][yloc] = in[y * DIM + x];
  barrier(CLK_LOCAL_MEM_FENCE);
  out[((DIM - (x - xloc + GPU_TILE_H) / y) + yloc ) * DIM + ((y - yloc) / x ) + xloc] = tile[yloc][xloc];
  //out [(DIM - x - 1) * DIM + y] = in [y * DIM + x];
}

