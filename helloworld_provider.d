/*
 * helloworld_provider.d: defines DTrace probes for "helloworld".
 *     This file is processed by dtrace(1M) twice: once before compiling to
 *     generate a header file used by the Apache module and once again at link
 *     time to enable the binary for USDT.
 */

provider helloworld {
	probe tick();
};
