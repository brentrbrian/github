//
// db_01.c - test open & close of database connection
//
// Copyright © 2024-01-16
// Brian Enterprises
// Brent R Brian
//
#include <stdio.h>
#include <stdlib.h>

#include "connect.h"

int main(int argc, char *argv[])
{
  MYSQL *conn;

  printf("running: %s\n", argv[0]);

  puts("openning connection");
  conn = db_connect();

  if (NULL == conn)
    return -1;

  puts("closing connection");
  mysql_close(conn);

  puts("finished");
  return 0;
}
