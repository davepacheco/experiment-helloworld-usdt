{
  'targets': [
    {
      'target_name': 'helloworld',
      'type': 'executable',
      'include_dirs': [ '<(PRODUCT_DIR)' ],
      'sources': [ 'src/main.c', 'src/dtrace.c', 'src/helloworld_provider.c' ]
    }
  ]
}
