
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

#include "convert.h"

static const uint16_t CR     = 0x000D;
static const uint16_t LF     = 0x000A;
static const uint16_t TAB    = 0x0009;
static const uint16_t ZEROES = 0x0000;

static struct
{
    bool     CR;
    bool     LF;
    bool     SKIP;
} sConvert;

//
// add junk data to list
//
static void convert_add_junk(convert_t data)
{
  int i;

  for (i=0; i < JUNK_MAX; i++)
  {
    if (sGlobals.s.junk_buf[i].u16 == data.u16)
      return;

    if (sGlobals.s.junk_buf[i].u16 == ZEROES)
    {
      sGlobals.s.junk_buf[i].u16 = data.u16;
      sGlobals.s.junk_idx++;
      return;
    }
  }
}


//
// output character or SKIP it
//
static convert_char_e convert_skip(convert_t data)
{

  if (data.u16 == LF)
  {
    sConvert.LF = true;
    return CONVERT_CHAR_KEEP;
  }

  if (data.u16 == TAB)
    return CONVERT_CHAR_KEEP;

  if (data.u16 == ZEROES)
    return CONVERT_CHAR_SKIP;

  if (data.u16 == CR)
  {
    sConvert.CR = true;
    return CONVERT_CHAR_SKIP;
  }

  if (data.u8[1] > 0x00 || (data.u8[0] < 0x20 || data.u8[0] > 0x7f))
  {
    convert_add_junk(data);
    return CONVERT_CHAR_SPACE;
  }

  return CONVERT_CHAR_KEEP;
}

//
// get an entire record FIELD,TAB,FIELD,TAB,NEWLINE
//
convert_record_e convert_getRecord(FILE *pIN)
{
    convert_t data;
    convert_char_e resp;
    uint16_t  len;

    memset(&sConvert, 0, sizeof(sConvert));
    memset(&sGlobals.s, 0, sizeof(sGlobals.s));

    sGlobals.tabs = 0;

    while (!sConvert.CR || !sConvert.LF)
    {
      len = fread(data.u8, 1, 2, pIN);

      if (len < 2)
        return CONVERT_RECORD_EOF;

      resp = convert_skip(data);

      if (CONVERT_CHAR_SKIP == resp)
        continue;

      if (sGlobals.s.data_idx >= DATA_MAX)
        return CONVERT_RECORD_OVERFLOW;

      if ('\t' == data.u8[0])
        sGlobals.tabs++;

      if (CONVERT_CHAR_SPACE == resp)
        data.u8[0] = ' ';

      sGlobals.s.data_buf[sGlobals.s.data_idx++] = data.u8[0];

    }

    if (sGlobals.s.junk_idx > 0)
      return CONVERT_RECORD_JUNK;

    return CONVERT_RECORD_OK;
}

