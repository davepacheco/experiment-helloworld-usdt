{
  'targets': [
    {
      'target_name': 'helloworld',
      'type': 'executable',
      'dependencies': [ 'dtrace_header' ],
      'include_dirs': [ '<(SHARED_INTERMEDIATE_DIR)' ],
      'sources': [ 'src/main.c', 'src/dtrace.c', 'src/helloworld_provider.c' ]
    }, {
      'target_name': 'dtrace_header',
      'type': 'none',
      'actions': [ {
        'action_name': 'dtrace_header',
        'inputs': [ 'src/helloworld_provider.d' ],
        'outputs': [ '<(SHARED_INTERMEDIATE_DIR)/helloworld_provider.h' ],
        'action': [ 'dtrace', '-xnolibs', '-h', '-o', '<@(_outputs)', '-s', '<@(_inputs)' ]
      } ]
    }, {
      'target_name': 'dtrace_object',
      'type': 'none',
      'actions': [ {
        'action_name': 'dtrace_object',
        'inputs': [ 'src/helloworld_provider.d', '<(PRODUCT_DIR)/obj.target/helloworld/src/dtrace.o' ],
        'outputs': [ '<(PRODUCT_DIR)/obj.target/helloworld/src/helloworld_provider.o' ],
        'action': [ 'dtrace', '-xnolibs', '-G', '-o', '<@(_outputs)', '-s', '<@(_inputs)' ]
      } ]
    }
  ]
}
