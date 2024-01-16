//
// connect.c - provide mysql connection object for db_xx binaries
//
// Copyright © 2024-01-16
// Brian Enterprises
// Brent R Brian
//

#include <stdio.h>
#include "connect.h"


MYSQL * db_connect(void)
{
   MYSQL *conn;
   
   printf("%s: %s()\n",__FILE__,__func__);

   if (!(conn = mysql_init(0)))
   {
      puts("unable to initialize connection struct");
      return NULL;
   }

   // Connect to the database
   if (!mysql_real_connect(conn, "pi3-database", "nc", "nc-only", "voters", 3306, NULL, 0) )
   {
      printf("error connecting to Server: %s\n", mysql_error(conn));
      mysql_close(conn);
      return NULL;
   }

   return conn;
}


