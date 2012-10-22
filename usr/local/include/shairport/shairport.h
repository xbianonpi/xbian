#ifndef __SHAIRPORT_H__
#define __SHAIRPORT_H__

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <openssl/bio.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include "socketlib.h"
#include <regex.h>
#include <sys/types.h>
#include <regex.h>
#include "ao.h"


#define HWID_SIZE 6
#define SHAIRPORT_LOG 1

#ifndef LOG_INFO
#define LOG_INFO     5
#endif

#ifndef LOG_DEBUG
#define LOG_DEBUG    6
#endif

#define LOG_DEBUG_V  7
#define LOG_DEBUG_VV 8

struct shairbuffer
{
  char *data;
  int   current;
  int   maxsize;
  int   marker;
};

struct keyring
{
  char *aeskey;
  char *aesiv;
  char *fmt;
};

struct comms
{
  int  in[2];
  int  out[2];
};

struct connection
{
  struct shairbuffer  recv;
  struct shairbuffer  resp;
  struct keyring      *keys; // Does not point to malloc'd memory.
#ifndef XBMC
  struct comms        *hairtunes;
#endif
  int                 clientSocket;
  char                *password;
};

#ifdef __cplusplus
extern "C"
{
#endif /* __cplusplus */

struct printfPtr
{
  int (*extprintf)(const char* msg, size_t msgSize);
};

int shairport_main(int argc, char **argv);
void shairport_exit(void);
int shairport_loop(void);
int shairport_is_running(void);
void shairport_set_ao(struct AudioOutput *ao);
void shairport_set_printf(struct printfPtr *funcPtr);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif

