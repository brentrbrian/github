//
// (C)opyright 2021 Brent R. Brian
//
// Convert UTF16 -> UTF8 and flag invalid ascii characters
//         for loading into database
//
// VoteNC - Voter registration analysis
//

#include <stdlib.h>
#include <string.h>

#include "convert.h"
#include "globals.h"

#define HEX_MAX (JUNK_MAX * 5)

static char HEX_CHR[16] = { '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F' };
static char HEX_BUF[HEX_MAX];


static void logger(FILE *pERR, char *msg)
{
  printf("%s\n", msg);
  fprintf(pERR, "%s\n", msg);
}


int main(int argc, char **argv)
{

  FILE *pIN, *pOUT, *pERR;
  size_t i, j, len, tot_len;
  convert_t cookie;
  convert_record_e result;

  pIN  = fopen("../../../data/VR_Snapshot_20240101.txt", "rb");
  pOUT = fopen("../../../data/VR_Snapshot_20240101_clean.txt", "w");
  pERR = fopen("../../../data/VR_Snapshot_20240101_err.txt", "w");

  logger(pERR, "************");
  logger(pERR, "* starting *");
  logger(pERR, "************");

  if (NULL == pIN)
  {
      logger(pERR, "The file is not opened. The program will now exit.");
      exit(1);
  }

  //
  // this conversion is for the DB dumps with a magic cookie of FEFF
  //

  len = fread(cookie.u8, 1, 2, pIN);

  if (0xFEFF != cookie.u16)
  {
      logger(pERR, "Magic cookie is invalid.");
      exit(2);
  }

  printf("%ld %04X\n", len, cookie.u16);

  tot_len = len;

  result = CONVERT_RECORD_OK;

  while (CONVERT_RECORD_EOF != result)
  {
    result = convert_getRecord(pIN);

    if (CONVERT_RECORD_OVERFLOW == result)
    {
      logger(pERR, "Error: overflow");
      break;
    }

    len = fwrite(sGlobals.s.data_buf, 1, sGlobals.s.data_idx, pOUT);

    if (len != sGlobals.s.data_idx)
    {
      logger(pERR, "Error: fwrite() did not output entire buffer");
      break;
    }

    if (CONVERT_RECORD_JUNK == result || sGlobals.tabs != 89)
    {

      //
      // print [JUNK_HEX] data for debugging data
      //

      memset(HEX_BUF, 0, sizeof(HEX_BUF));

      for (i = 0, j = 1; i < sGlobals.s.junk_idx; i++)
      {
        HEX_BUF[j++] = HEX_CHR[sGlobals.s.junk_buf[i].nibbles.N3];
        HEX_BUF[j++] = HEX_CHR[sGlobals.s.junk_buf[i].nibbles.N2];
        HEX_BUF[j++] = HEX_CHR[sGlobals.s.junk_buf[i].nibbles.N1];
        HEX_BUF[j++] = HEX_CHR[sGlobals.s.junk_buf[i].nibbles.N0];
        HEX_BUF[j++] = ' ';
      }

      if (j>2)
      {
        HEX_BUF[0]   = '[';
        HEX_BUF[j-1] = ']';
        HEX_BUF[j]   = ' ';
      }

      (void) fwrite(HEX_BUF, 1, strlen(HEX_BUF), pERR);
      (void) fwrite(sGlobals.s.data_buf, 1, sGlobals.s.data_idx, pERR);
      (void) fwrite("\n\n", 1, 2, pERR);

    }

    tot_len += len;
  }

  printf("total length %15ld\n", tot_len);

  logger(pERR, "************");
  logger(pERR, "* finished *");
  logger(pERR, "************");

  fclose(pIN);
  fclose(pOUT);
  fclose(pERR);

  return 0;
}
