## learning on lmdb

### features

- Ordered map interface (keys are always lexicographically sorted).


- Reader/writer transactions: readers don’t block writers, writers don’t block readers. Each environment supports one concurrent write transaction.

- Read transactions are extremely cheap.
- Environments may be opened by multiple processes on the same host, making it ideal for working around Python’s GIL.

- Multiple named databases may be created with transactions covering all named databases.

- Memory mapped, allowing for zero copy lookup and iteration. This is optionally exposed to Python using the buffer() interface

- Maintenance requires no external process or background threads.

- No application-level caching is required: LMDB fully exploits the operating system’s buffer cache.
