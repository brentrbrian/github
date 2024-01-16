//
// db_02.c - simple query to return mysql version number
//
// Copyright © 2024-01-16
// Brian Enterprises
// Brent R Brian
//
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <string.h>

#include "connect.h"

#define STR_FMT "%-10s %-25s %-20s %-20s %-5s %-5s"

/*
  query to print first 10 records from voter registration table

  ---------- ------------------------- -------------------- -------------------- ----- -----
  NC_ID      LAST_NAMT                 FIRST_NAME           MIDDLE_NAME          SEX   RACE
  ---------- ------------------------- -------------------- -------------------- ----- -----
  AA2036     AARON                     CLAUDIA              HAYDEN               F     W
  AA2040     ABBOTT                    EARL                 RANDOLPH             M     B
  AA2047     ABERCROMBIE               EDWIN                GRAY                 M     W
  AA2056     ABERNATHY                 JEFFERSON            REID                 M     W
  AA2092     ADAMS                     BILLY                DAN                  M     W
  AA2093     ADAMS                     BOBBY                JOE                  M     W
  AA2106     ADAMS                     FRANKIE              WARREN               F     W
  AA2126     ADAMS                     LATTA                COLETTE              F     B
  AA2128     ADAMS                     LUCILLE              ANDREWS              F     W
  AA2149     ADAMS                     TERESA               BALDWIN              F     W
  ---------- ------------------------- -------------------- -------------------- ----- -----
*/

int do_query(void)
{
  MYSQL       *mysql;
  MYSQL_RES   *result;
  MYSQL_ROW    row;
  int          err;
  char        *query;
  uint64_t     i, rows;
  char         strHDR[128], strLINE[128];

  printf("%s()\n", __func__);

  puts("db_connect()");
  mysql = db_connect();

  if (!mysql)
    return -1;

  query = "SELECT r.NC_ID, \
                  r.NAME_LAST, \
                  r.NAME_FIRST, \
                  r.NAME_MIDDLE, \
                  r.SEX_CODE, \
                  r.RACE_CODE  \
           FROM voters.reg_2020_11_03 r \
           LIMIT 10;";

  puts("mysql_query()");
  err = mysql_query(mysql, query);

  if (err)
    return -2;

  puts("mysql_store_result()");
  result = mysql_store_result(mysql);

  if (NULL == result)
    return -3;

  rows = mysql_num_rows(result);

  printf("mysql_fetch_row() %" PRIu64 "\n", rows);

  if (rows)
  {
    sprintf(strLINE, STR_FMT, "----------",
                              "-------------------------",
                              "--------------------",
                              "--------------------",
                              "-----",
                              "-----");

    sprintf(strHDR, STR_FMT, "NC_ID",
                             "LAST_NAMT",
                             "FIRST_NAME",
                             "MIDDLE_NAME",
                             "SEX",
                             "RACE");

    puts(strLINE);
    puts(strHDR);
    puts(strLINE);

    for (i = 0; i < rows; i++)
    {
      row = mysql_fetch_row(result);

      if (NULL == row)
        return -4;

      printf(STR_FMT "\n", row[0], row[1], row[2], row[3], row[4], row[5]);
    }

    puts(strLINE);
  }

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
