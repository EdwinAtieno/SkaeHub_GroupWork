# SkaeHub_GroupWork
1)	Definition- SQLite is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
2)	Application:
If portability is of a concern, go with SQLite. This makes the transfer of all your database data much more efficient as it is stored in a single file. Furthermore, if your application requires that you write to disk locally you may also want to use SQLite.
However, if you require scalability in terms of the number of database queries required, MySQL is the better choice. If you want any real degree of concurrency or require higher levels of security as well as user permissions management, MySQL wins over SQLite.

3)	SQLite Advantages
•	Lightweight-SQLite is a very light weighted database so, it is easy to use it as an embedded software with devices like televisions, Mobile phones, cameras, home electronic devices, etc
•	
Better Performance-Reading and writing operations are very fast for SQLite database. It is almost 35% faster than File system. It only loads the data which is needed, rather than reading the entire file and hold it in memory.
•	
No Installation Needed-You don’t need to install and configure it. Just download SQLite libraries in your computer and it is ready for creating the database.
•	
Portable-SQLite is portable across all 32-bit and 64-bit operating systems and big- and little-endian architectures.
•	
Accessible-SQLite database is accessible through a wide variety of third-party tools.
•	
Reduce Cost and Complexity-It reduces application cost because content can be accessed and updated using concise SQL queries instead of lengthy and error-prone procedural queries.
4)	SQLite Disadvantages
•	SQLite is used to handle low to medium traffic HTTP requests.
•	Database size is restricted to 2GB in most cases.
•	No built in data encryption methods/ techniques
5)	Features:
•	Serverless- Programs that want to access the database communicate with the server using some kind of inter-process communication (typically TCP/IP) to send requests to the server and to receive back results. SQLite does not work this way. With SQLite, the process that wants to access the database reads and writes directly from the database files on disk. There is no intermediary server process.
•	Stable Cross-Platform Database File- A database file written on one machine can be copied to and used on a different machine with a different architecture
•	.Compact-When optimized for size, the whole SQLite library with everything enabled is less than 500KiB in size (as measured on an ix86 using the "size" utility from the GNU compiler suite.) Unneeded features can be disabled at compile-time to further reduce the size of the library to under 300KiB if desired.
•	Manifest typing-SQLite thus allows the user to store any value of any datatype into any column regardless of the declared type of that column. (There are some exceptions to this rule: An INTEGER PRIMARY KEY column may only store integers.
