#!/usr/bin/env python3

Y, N = True, False

full_list = {
    # (filename,                                              bm1684x, bm1688, bm1690, sg2380, sg2262, masr3)
    #                                                         [base, full]
    "regression/unittest/arith":
      [("arith_int.pl",                                        Y,       Y,      Y,      N,      Y,     N),
       ("add_pipeline_bm1688.pl",                              N,       N,      N,      N,      Y,     N),],
    "regression/unittest/arith_int":
      [("c_sub_int.pl",                                        N,       N,      N,      N,      Y,     N),],
    "regression/unittest/attention":
      [("rotary_embedding_static.pl",                          N,       N,      N,      N,      N,     N),
       ("mlp_left_trans_multicore.pl",                         N,       N,      Y,      N,      N,     N)],
    "regression/unittest/cmp":
      [("greater_fp16.pl",                                     Y,       N,      N,      N,      Y,     N),
       ("equal_int16.pl",                                      Y,       N,      N,      N,      N,     Y),],
    "regression/unittest/conv":
      [("Conv2D.pl",                                           Y,       N,      Y,      N,      N,     N),
       ("depthwise2d_int8.pl",                                 Y,       N,    [N,Y],    N,      N,     N),
       ("quant_conv2d_for_deconv2d_int8_asym_int16_int8.pl",   Y,       N,      Y,      N,      Y,     N),],
    "regression/unittest/divide":
      [("fp32_tunable_div_multi_core.pl",                      N,       N,      Y,      N,      N,     N),],
    "regression/unittest/dma":
      [("move_s2s_fp32.pl",                                  [N,Y],     N,      N,      N,      Y,     N),
       ("move_l2l_fp32.pl",                                    N,       N,      N,      N,      Y,     N),
       ("dmaload_nc_trans_f32.pl",                             N,       N,      N,      N,      N,     N),
       ("dmastore_nc_trans_f32.pl",                            N,       N,      N,      N,      Y,     N),
       ("dmaload_bc_S2L_fp32.pl",                              N,       N,      N,      N,      Y,     N),
       ("dmaload_bc_L2L_fp32.pl",                              N,       N,      N,      N,      N,     N),
       ("dma_nonzero_l2s.pl",                                [N,Y],     N,      N,      N,      Y,     N),
       ("dma_nonzero_s2s.pl",                                [N,Y],     N,      N,      N,      Y,     N),],
    "regression/unittest/gather_scatter":
      [("batch_bcast_w_scatter_fp16.pl",                     [N,Y],     N,      N,      N,      Y,     N),
       ("h_scatter_s2s_index_local_bf16.pl",                 [N,Y],     N,      N,      N,      Y,     N),
       ("hw_gather_bf16.pl",                                 [N,Y],     N,      N,      N,      Y,     N),
       ("hw_scatter_bf16.pl",                                [N,Y],     N,      N,      N,      Y,     N),
       ("w_gather_bf16.pl",                                  [N,Y],     N,      N,      N,      Y,     N),
       ("w_scatter_bf16.pl",                                   Y,       N,      N,      N,      Y,     N),],
    "regression/unittest/hau":
      [("hau_sort_2d.pl",                                      N,       N,      N,      N,      N,     N),
       ("topk.pl",                                             N,       N,      N,      N,      N,     N),
       ("hau.pl",                                              Y,       N,      N,      N,      N,     N),
       ("hau_poll.pl",                                         Y,       N,      Y,      N,      N,     N),],
    "regression/unittest/mask":
      [("mask_select_batch_bcast_bf16_multi_core.pl",          Y,       N,      N,      N,      Y,     N),],
    "regression/unittest/matmul":
      [("mm2_int8_all_trans.pl",                             [N,Y],     N,      N,      N,      Y,     N),
       ("mm_fp32.pl",                                        [N,Y],     N,      N,      N,      Y,     N),],
    "regression/unittest/npu":
      [("npu_bcast_fp16.pl",                                 [N,Y],     N,      N,      N,      Y,     N),],
    "regression/unittest/round":
      [("round_bf16.pl",                                     [N,Y],     N,      N,      N,      Y,     N),],
    "regression/unittest/rqdq":
      [("rq_fp_int8_uint16.pl",                                Y,     [N,Y],   [N,Y],   N,    [Y,Y],   N),],
    "regression/unittest/scalebias":
      [("fp_scale_bias_bf16.pl",                             [N,Y],     N,      N,      N,      Y,     N),],
    "regression/unittest/tiu_trans":
      [("cw_trans.pl",                                         N,       N,    [N,Y],    N,      Y,     Y),],
    "regression/unittest/sdma":
      [("sdma.pl",                                             N,       N,      Y,      N,      N,     N),],
    "regression/unittest/unary":[],
    "examples/cxx/arith":
      [("add_c_dual_loop.pl",                                  N,       N,      N,      N,      N,     N),
       ("add_dyn_block.pl",                                    Y,       Y,      Y,      N,      Y,     N),
       ("add_pipeline.pl",                                     N,       N,    [N,Y],    N,      N,     N),
       ("add_broadcast.pl",                                    N,       N,    [N,Y],    N,    [N,Y],   N),],
    "examples/cxx/llm":
      [("attention_dyn.pl",                                    Y,       Y,      Y,      N,      N,     N),
       ("flash_attention.pl",                                  N,       N,      N,      N,      Y,     N),
       ("rmsnorm.pl",                                        [N,Y],     N,      N,      N,      Y,     N),
       ("swi_glu.pl",                                        [N,Y],     N,      N,      N,      Y,     N),
       ("flash_attention_backward_multicore.pl",               N,       N,    [N,Y],    N,      Y,     N),
       ("flash_attention_GQA_multicore.pl",                    N,       N,      Y,      N,      Y,     N),],
    "examples/cxx/matmul":
      [("mm2_fp16_sync.pl",                                    N,       N,      Y,      N,      N,     N),
       ("mm.pl",                                             [N,Y],     N,      N,      N,      Y,     N),
       ("mm2_int.pl",                                          Y,       N,      N,      N,      N,     N),
       ("mm2_float.pl",                                        Y,       N,      N,      N,      Y,     N),],
    "regression/unittest/fileload":
      [("test_read.pl",                                        Y,       N,      N,      N,      Y,     N),],
    "regression/unittest/pool":
      [("avg_pool2d.pl",                                     [N,Y],     N,      N,      N,      Y,     N),],
    "examples/cxx/activation":
      [("softmax_h_dim.pl",                                    Y,       N,    [N,Y],    N,    [Y,Y],   N),],
    "regression/unittest/func":
      [("sin.pl",                                              Y,       N,      N,      N,      Y,     N),
       ("cos.pl",                                              Y,       N,      N,      N,      Y,     N),
       ("arcsin.pl",                                         [N,Y],     N,      N,      N,      Y,     N),
       ("arccos.pl",                                         [N,Y],     N,      N,      N,      Y,     N),
       ("tan.pl",                                              Y,       N,      N,      N,      Y,     N),
       ("cot.pl",                                              Y,       N,      N,      N,      Y,     N),
       ("sqrt.pl",                                           [N,Y],     N,      N,      N,    [Y,Y],   N),
       ("sqrt_mars3_bf16.pl",                                [N,Y],     N,      N,      N,    [Y,Y],   Y),
       ("relu.pl",                                           [N,Y],     N,      N,      N,      Y,     N),
       ("prelu.pl",                                          [N,Y],     N,      N,      N,      Y,     N),
       ("exp.pl",                                            [N,Y],     N,      N,      N,      Y,     N),
       ("softplus.pl",                                       [N,Y],     N,      N,      N,      Y,     N),
       ("mish.pl",                                           [N,Y],     N,      N,      N,      Y,     N),
       ("sinh.pl",                                           [N,Y],     N,      N,      N,      Y,     N),
       ("cosh.pl",                                           [N,Y],     N,      N,      N,      Y,     N),
       ("tanh.pl",                                           [N,Y],     N,      N,      N,      Y,     N),
       ("arcsinh.pl",                                        [N,Y],     N,      N,      N,      Y,     N),
       ("arccosh.pl",                                        [N,Y],     N,      N,      N,      Y,     N),
       ("arctanh.pl",                                        [N,Y],     N,      N,      N,      Y,     N),
       ("softsign.pl",                                       [N,Y],     N,      N,      N,      Y,     N),],
}

sample_list = {
    # (filename,                      bm1684x, bm1688, bm1690, sg2380, sg2262, mars3)
    "samples/add_pipeline":
      [("test",                       Y,       N,      Y,      N,      N,      N),],
    "samples/llama2":
      [("test",                       Y,       N,      N,      N,      N,      N),],
    "regression/unittest/tpu_mlir":
      [("test",                       Y,       N,      N,      N,      N,      N),],
}

python_list = {
    # (filename,                      bm1684x, bm1688, bm1690, sg2380, sg2262, mars3)
    "examples/python":
      [("01-element-wise.py",            Y,       Y,      Y,      N,      Y,   N),
       ("01-element-wise-bm1684x.py",    Y,       N,      N,      N,      N,   N),
       ("02-avg-max-pool.py",            Y,       N,      N,      N,      N,   N),
       ("02-min-pool.py",                N,       N,      N,      N,      N,   N),
       ("03-conv.py",                    N,       N,      N,      N,      Y,   N),
       ("03-conv-bm1688.py",             N,       N,      N,      N,      N,   N),
       ("04-matmul.py",                  Y,       N,      N,      N,      N,   N),
       ("04-matmul-bm1688.py",           N,       N,      N,      N,      N,   N),
       ("05-attention-GQA.py",           Y,       N,      Y,      N,      Y,   N),
       ("06-gather-scatter.py",          Y,       N,      N,      N,      N,   N),
       ("07-arange_broadcast.py",        Y,       N,      N,      N,      N,   N),
       ("09-dma.py",                     Y,       N,      N,      N,      N,   N),
       ("10-vc-op.py",                   Y,       N,      N,      N,      N,   N),
       ("11-tiu-transpose.py",           Y,       N,      N,      N,      N,   N),
       ("13-hau.py",                     Y,       N,      N,      N,      N,   N),
       ("14-sdma.py",                    N,       N,      N,      N,      N,   N),
       ("15-rq-dq.py",                   Y,       N,      N,      N,      Y,   N),
       ("15-rq-dq-bm1688-bm1690.py",     N,       N,      N,      N,      N,   N),
       ("16-multicore.py",               N,       N,      Y,      N,      Y,   N),
       ("17-uint.py",                    Y,       Y,      Y,      N,      N,   N),
       ("19_autotiling.py",              N,       N,      Y,      N,      N,   N),],
}
