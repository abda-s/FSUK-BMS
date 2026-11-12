/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2026 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32g4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define ISENSE_HI_ADC_Pin GPIO_PIN_0
#define ISENSE_HI_ADC_GPIO_Port GPIOC
#define ISENSE_LO_ADC_Pin GPIO_PIN_1
#define ISENSE_LO_ADC_GPIO_Port GPIOC
#define ISENSE_SUPPLY_ADC_Pin GPIO_PIN_2
#define ISENSE_SUPPLY_ADC_GPIO_Port GPIOC
#define BQ_nCS_Pin GPIO_PIN_4
#define BQ_nCS_GPIO_Port GPIOA
#define BQ_SCLK_Pin GPIO_PIN_5
#define BQ_SCLK_GPIO_Port GPIOA
#define BQ_MISO_Pin GPIO_PIN_6
#define BQ_MISO_GPIO_Port GPIOA
#define BQ_MOSI_Pin GPIO_PIN_7
#define BQ_MOSI_GPIO_Port GPIOA
#define BQ_NFAULT_Pin GPIO_PIN_0
#define BQ_NFAULT_GPIO_Port GPIOB
#define BQ_NFAULT_EXTI_IRQn EXTI0_IRQn
#define BQ_SPI_RDY_Pin GPIO_PIN_1
#define BQ_SPI_RDY_GPIO_Port GPIOB
#define CHG_EN_Pin GPIO_PIN_6
#define CHG_EN_GPIO_Port GPIOC
#define AMS_OK_MCU_Pin GPIO_PIN_7
#define AMS_OK_MCU_GPIO_Port GPIOC
#define BAL_EN_N_Pin GPIO_PIN_8
#define BAL_EN_N_GPIO_Port GPIOC

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
