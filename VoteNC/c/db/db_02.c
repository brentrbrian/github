//
// db_02.c - simple query to return mysql version number
//
// Copyright © 2024-01-16
// Brian Enterprises
// Brent R Brian
//
#include <stdio.h>
#include <stdlib.h>

#include "connect.h"

int do_query(void)
{
  MYSQL       *mysql;
  MYSQL_RES   *result;
  MYSQL_ROW    row;
  int          err;

  printf("%s()\n", __func__);

  puts("db_connect()");
  mysql = db_connect();

  if (!mysql)
    return -1;

  puts("mysql_query()");
  err = mysql_query(mysql, "SELECT VERSION();");

  if (err)
    return -2;

  puts("mysql_store_result()");
  result = mysql_store_result(mysql);

  if (NULL == result)
    return -3;

  puts("mysql_fetch_row()");
  row = mysql_fetch_row(result);

  if (NULL == row)
    return -4;

  printf("VERSION() %s\n", row[0]);

  puts("closing connection");
  mysql_close(mysql);

  return 0;
}

int main(int argc, char *argv[])
{
  int err;

  puts("******************************");
  printf("%s\n", argv[0]);
  puts("******************************");

  err = do_query();

  if (err)
    printf("do_main() returned %d\n", err);

  printf("finished: %s\n", argv[0]);

  exit(err);

}
