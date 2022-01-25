/*************************************************************************
 *
 *    Used with ICCARM and AARM.
 *
 *    (c) Copyright IAR Systems 2006
 *
 *    File name   : stm32f_usb_cfg.h
 *    Description : USB definitions
 *
 *    History :
 *    1. Date        : February 10, 2006
 *       Author      : Stanimir Bonev
 *       Description : Create
 *
 *    $Revision: 1.2.2.4 $
 **************************************************************************/

#include "includes.h"

#ifndef __STM32F_USB_CFG_H
#define __STM32F_USB_CFG_H

/* USB Events */
#define USB_SOF_EVENT             0
#define USB_ERROR_EVENT           0   // for debug
#define USB_HIGH_PRIORITY_EVENT   0   // ISO and Double buffered bulk
#define USB_DOVR_EVENT            0   // for speed up retransfer

#define USB_REMOTE_WAKEUP         1   // Remote wake-up event (device to host)
/* Endpoint definitions */
#define Ep0MaxSize        			  8

#define ReportEp                  UsbEp1In
#define ReportEpMaxSize           8

#define MaxIndOfRealizeEp         1

/* Other definitions */
#define USB_TRACE_LM_EN     1
#define USB_TRACE_LW_EN     1
#define USB_TRACE_LE_EN     1
#define USB_TRACE_T9M_EN    0
#define USB_TRACE_T9W_EN    1
#define USB_TRACE_T9E_EN    1

#endif //__STM32F_USB_CFG_H
