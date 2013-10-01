/*      $Id: lirc_client.h,v 5.11 2008/05/20 18:54:37 lirc Exp $      */

/****************************************************************************
 ** lirc_client.h ***********************************************************
 ****************************************************************************
 *
 * lirc_client - common routines for lircd clients
 *
 * Copyright (C) 1998 Trent Piepho <xyzzy@u.washington.edu>
 * Copyright (C) 1998 Christoph Bartelmus <lirc@bartelmus.de>
 *
 */

#ifndef LIRC_CLIENT_H
#define LIRC_CLIENT_H

#include <stddef.h>
#include <stdint.h>

#ifndef __u32
typedef uint32_t __u32;
#endif

#ifdef __cplusplus
extern "C" {
#endif

#define LIRC_RET_SUCCESS  (0)
#define LIRC_RET_ERROR   (-1)

#define LIRC_ALL ((char *) (-1))

	enum lirc_flags { none = 0x00,
		once = 0x01,
		quit = 0x02,
		mode = 0x04,
		ecno = 0x08,
		startup_mode = 0x10,
		toggle_reset = 0x20,
	};

	struct lirc_list {
		char *string;
		struct lirc_list *next;
	};

	struct lirc_code {
		char *remote;
		char *button;
		struct lirc_code *next;
	};

	struct lirc_config {
		char *current_mode;
		struct lirc_config_entry *next;
		struct lirc_config_entry *first;

		int sockfd;
	};

	struct lirc_config_entry {
		char *prog;
		struct lirc_code *code;
		unsigned int rep_delay;
		unsigned int rep;
		struct lirc_list *config;
		char *change_mode;
		unsigned int flags;

		char *mode;
		struct lirc_list *next_config;
		struct lirc_code *next_code;

		struct lirc_config_entry *next;
	};

	int lirc_init(char *prog, int verbose);
	int lirc_deinit(void);

	int lirc_readconfig(char *file, struct lirc_config **config, int (check) (char *s));
	void lirc_freeconfig(struct lirc_config *config);

/* obsolete */
	char *lirc_nextir(void);
/* obsolete */
	char *lirc_ir2char(struct lirc_config *config, char *code);

	int lirc_nextcode(char **code);
	int lirc_code2char(struct lirc_config *config, char *code, char **string);

/* new interface for client daemon */
	int lirc_readconfig_only(char *file, struct lirc_config **config, int (check) (char *s));
	int lirc_code2charprog(struct lirc_config *config, char *code, char **string, char **prog);
	size_t lirc_getsocketname(const char *filename, char *buf, size_t size);
	const char *lirc_getmode(struct lirc_config *config);
	const char *lirc_setmode(struct lirc_config *config, const char *mode);

#ifdef __cplusplus
}
#endif
#endif
