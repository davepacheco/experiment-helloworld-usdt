{
  'targets': [
    {
      'target_name': 'helloworld',
      'type': 'executable',
      'sources': [ 'src/main.c' ],
      'dependencies': [ 'helloworld_provider_o', 'dtrace_o' ],
    },
    {
      'target_name': 'dtrace_o',
      'type': 'static_library',
      'include_dirs': [ '<(SHARED_INTERMEDIATE_DIR)' ],
      'sources': [
        '<(SHARED_INTERMEDIATE_DIR)/helloworld_provider.h',
        'src/dtrace.c'
      ],
      'dependencies': [ 'helloworld_provider_h' ],
    },
    {
      'target_name': 'helloworld_provider_h',
      'type': 'none',
      'actions': [ {
        'action_name': 'helloworld_provider_h',
        'inputs': [ 'src/helloworld_provider.d' ],
        'outputs': [ '<(SHARED_INTERMEDIATE_DIR)/helloworld_provider.h' ],
        'action': [
          'dtrace', '-h', '-xnolibs', '-s', '<@(_inputs)', '-o', '<@(_outputs)'
        ]
      } ]
    },
    {
      'target_name': 'helloworld_provider_o',
      'type': 'none',
      'dependencies': [ 'helloworld_provider_h', 'dtrace_o' ],
      'direct_dependent_settings': {
        'libraries': [ '<(SHARED_INTERMEDIATE_DIR)/helloworld_provider.o' ]
      },
      'actions': [ {
        'action_name': 'helloworld_provider_o',
        'outputs': [ '<(SHARED_INTERMEDIATE_DIR)/helloworld_provider.o' ],
        'inputs': [
          'src/helloworld_provider.d',
          '<(PRODUCT_DIR)/obj.target/dtrace_o/src/dtrace.o'
        ],
        'action': [ 'dtrace', '-G', '-xnolibs', '-s', '<@(_inputs)',
          '-o', '<@(_outputs)' ]
      } ]
    }
  ]
}
