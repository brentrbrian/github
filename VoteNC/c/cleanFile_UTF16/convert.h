

#ifndef __CONVERT_H__
#define __CONVERT_H__

#include <stdio.h>

#include "globals.h"

typedef enum
{
  CONVERT_CHAR_KEEP = 0,
  CONVERT_CHAR_SKIP,
  CONVERT_CHAR_SPACE
} convert_char_e;

typedef enum
{
  CONVERT_RECORD_OK = 0,
  CONVERT_RECORD_EOF,
  CONVERT_RECORD_OVERFLOW,
  CONVERT_RECORD_JUNK
} convert_record_e;

convert_record_e convert_getRecord(FILE *pIN);

#endif // __CONVERT_H__
