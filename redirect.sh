#!/bin/bash
if [ "${CONFCACHE_DEBUG}" ]; then
	unset CONFCACHE_DEBUG
	set -x
fi
for x in ${CONFCACHE_RESETS}; do
	cf="CONFCACHE_${x}"
	if [ "${!cf}" ]; then
		export ${x}="${!x}${!x:+:}${!cf}"
		unset "${cf}" &> /dev/null
	fi
done
unset cf &> /dev/null
if [ "${CONFCACHE_DIR_RESET}" ]; then
	cd "${CONFCACHE_DIR_RESET}"
	unset CONFCACHE_DIR_RESET
fi
export SANDBOX_ON=1
exec "$@"
