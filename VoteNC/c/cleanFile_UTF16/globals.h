
#ifndef __GLOBALS_H__
#define __GLOBALS_H__

#include <stdio.h>
#include <stdint.h>

#define JUNK_MAX   16
#define DATA_MAX   4096

typedef struct
{
  uint16_t   N0 : 4,
             N1 : 4,
             N2 : 4,
             N3 : 4;
} nibbles_t;

typedef union
{
  nibbles_t nibbles;
  uint16_t  u16;
  uint8_t   u8[2];
} convert_t;

typedef struct
{
  struct
  {
    char      data_buf[DATA_MAX];
    uint16_t  data_idx;
    convert_t junk_buf[JUNK_MAX];
    uint16_t  junk_idx;
  } s;

  uint8_t   tabs;
} globals_t;

extern globals_t sGlobals;

#endif // __GLOBALS_H__
