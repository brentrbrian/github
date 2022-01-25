//*****************************************************************************
//
// startup_gcc.c - Startup code for use with GNU tools.
//
// Copyright (c) 2009-2012 Texas Instruments Incorporated.  All rights reserved.
// Software License Agreement
// 
// Texas Instruments (TI) is supplying this software for use solely and
// exclusively on TI's microcontroller products. The software is owned by
// TI and/or its suppliers, and is protected under applicable copyright
// laws. You may not combine this software with "viral" open-source
// software in order to form a larger program.
// 
// THIS SOFTWARE IS PROVIDED "AS IS" AND WITH ALL FAULTS.
// NO WARRANTIES, WHETHER EXPRESS, IMPLIED OR STATUTORY, INCLUDING, BUT
// NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE. TI SHALL NOT, UNDER ANY
// CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL, OR CONSEQUENTIAL
// DAMAGES, FOR ANY REASON WHATSOEVER.
// 
// This is part of revision 9453 of the DK-LM3S9D96 Firmware Package.
//
//*****************************************************************************

//*****************************************************************************
//
// Forward declaration of the default fault handlers.
//
//*****************************************************************************
void ResetISR(void);
static void NmiISR(void);
static void FaultISR(void);
static void IntDefaultHandler(void);

//*****************************************************************************
//
// The entry point for the application.
//
//*****************************************************************************
extern int main(void);

//*****************************************************************************
//
// Reserve space for the system stack.
//
//*****************************************************************************
static unsigned long pulStack[64];

//*****************************************************************************
//
// The vector table.  Note that the proper constructs must be placed on this to
// ensure that it ends up at physical address 0x0000.0000.
//
//*****************************************************************************
__attribute__ ((section(".isr_vector")))
void (* const g_pfnVectors[])(void) =
{
    (void (*)(void))((unsigned long)pulStack + sizeof(pulStack)),
                                            // The initial stack pointer
    ResetISR,                               // The reset handler
    NmiISR,                                 // The NMI handler
    FaultISR,                               // The hard fault handler
    IntDefaultHandler,                      // The MPU fault handler
    IntDefaultHandler,                      // The bus fault handler
    IntDefaultHandler,                      // The usage fault handler
    0,                                      // Reserved
    0,                                      // Reserved
    0,                                      // Reserved
    0,                                      // Reserved
    IntDefaultHandler,                      // SVCall handler
    IntDefaultHandler,                      // Debug monitor handler
    0,                                      // Reserved
    IntDefaultHandler,                      // The PendSV handler
    IntDefaultHandler,                      // The SysTick handler
    IntDefaultHandler,                      //  WWDG_IRQHandler
    IntDefaultHandler,                      //  PVD_IRQHandler
    IntDefaultHandler,                      //  TAMPER_IRQHandler
    IntDefaultHandler,                      //  RTC_IRQHandler
    IntDefaultHandler,                      //  FLASH_IRQHandler
    IntDefaultHandler,                      //  RCC_IRQHandler
    IntDefaultHandler,                      //  EXTI0_IRQHandler
    IntDefaultHandler,                      //  EXTI1_IRQHandler
    IntDefaultHandler,                      //  EXTI2_IRQHandler
    IntDefaultHandler,                      //  EXTI3_IRQHandler
    IntDefaultHandler,                      //  EXTI4_IRQHandler
    IntDefaultHandler,                      //  DMAChannel1_IRQHandler
    IntDefaultHandler,                      //  DMAChannel2_IRQHandler
    IntDefaultHandler,                      //  DMAChannel3_IRQHandler
    IntDefaultHandler,                      //  DMAChannel4_IRQHandler
    IntDefaultHandler,                      //  DMAChannel5_IRQHandler
    IntDefaultHandler,                      //  DMAChannel6_IRQHandler
    IntDefaultHandler,                      //  DMAChannel7_IRQHandler
    IntDefaultHandler,                      //  ADC_IRQHandler
    IntDefaultHandler,                      //  USB_HP_CAN_TX_IRQHandler
    IntDefaultHandler,                      //  USB_LP_CAN_RX0_IRQHandler
    IntDefaultHandler,                      //  CAN_RX1_IRQHandler
    IntDefaultHandler,                      //  CAN_SCE_IRQHandler
    IntDefaultHandler,                      //  EXTI9_5_IRQHandler
    IntDefaultHandler,                      //  TIM1_BRK_IRQHandler
    IntDefaultHandler,                      //  TIM1_UP_IRQHandler
    IntDefaultHandler,                      //  TIM1_TRG_CCUP_IRQHandler
    IntDefaultHandler,                      //  TIM1_CC_IRQHandler
    IntDefaultHandler,                      //  TIM2_IRQHandler
    IntDefaultHandler,                      //  TIM3_IRQHandler
    IntDefaultHandler,                      //  TIM4_IRQHandler
    IntDefaultHandler,                      //  I2C1_EV_IRQHandler
    IntDefaultHandler,                      //  I2C1_ER_IRQHandler
    IntDefaultHandler,                      //  I2C2_EV_IRQHandler
    IntDefaultHandler,                      //  I2C2_ER_IRQHandler
    IntDefaultHandler,                      //  SPI1_IRQHandler
    IntDefaultHandler,                      //  SPI2_IRQHandler
    IntDefaultHandler,                      //  USART1_IRQHandler
    IntDefaultHandler,                      //  USART2_IRQHandler
    IntDefaultHandler,                      //  USART3_IRQHandler
    IntDefaultHandler,                      //  EXTI15_10_IRQHandler
    IntDefaultHandler,                      //  RTCAlarm_IRQHandler
    IntDefaultHandler                       //  USBWakeUp_IRQHandler
};

//*****************************************************************************
//
// The following are constructs created by the linker, indicating where the
// the "data" and "bss" segments reside in memory.  The initializers for the
// for the "data" segment resides immediately following the "text" segment.
//
//*****************************************************************************
extern unsigned long _etext;
extern unsigned long _data;
extern unsigned long _edata;
extern unsigned long _bss;
extern unsigned long _ebss;

//*****************************************************************************
//
// This is the code that gets called when the processor first starts execution
// following a reset event.  Only the absolutely necessary set is performed,
// after which the application supplied entry() routine is called.  Any fancy
// actions (such as making decisions based on the reset cause register, and
// resetting the bits in that register) are left solely in the hands of the
// application.
//
//*****************************************************************************
void ResetISR(void)
{
    unsigned long *pulSrc, *pulDest;

    //
    // Copy the data segment initializers from flash to SRAM.
    //
    pulSrc = &_etext;
    for(pulDest = &_data; pulDest < &_edata; )
    {
      *pulDest++ = *pulSrc++;
    }

    //
    // Zero fill the bss segment.
    //
    __asm("    ldr     r0,=_bss\n"
          "    ldr     r1,=_ebss\n"
          "    mov     r2,#0\n"
          "    .thumb_func\n"
          "zero_loop:\n"
          "    cmp     r0,r1\n"
          "    it      lt\n"
          "    strlt   r2,[r0], #4\n"
          "    blt     zero_loop");

    //
    // Call the application's entry point.
    //
    main();
}

//*****************************************************************************
//
// This is the code that gets called when the processor receives a NMI.  This
// simply enters an infinite loop, preserving the system state for examination
// by a debugger.
//
//*****************************************************************************
static void NmiISR(void)
{
    while(1)
    {
    }
}

//*****************************************************************************
//
// This is the code that gets called when the processor receives a fault
// interrupt.  This simply enters an infinite loop, preserving the system state
// for examination by a debugger.
//
//*****************************************************************************
static void FaultISR(void)
{
    while(1)
    {
    }
}

//*****************************************************************************
//
// This is the code that gets called when the processor receives an unexpected
// interrupt.  This simply enters an infinite loop, preserving the system state
// for examination by a debugger.
//
//*****************************************************************************
static void IntDefaultHandler(void)
{
    while(1)
    {
    }
}
