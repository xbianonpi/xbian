_xbian-config()
{
	local cur prev opts
	COMPREPLY=();
	cur="${COMP_WORDS[COMP_CWORD]}"
	prev="${COMP_WORDS[COMP_CWORD-1]}"
	if [ -d "/usr/local/include/xbian-config/modules/${prev}" ]; then
		arguments=$(grep ARGUMENTS "/usr/local/include/xbian-config/modules/${prev}/main" | sed -ne 's/\(.*\)\((\)\(.*\)\().*\)/\3/p');
		COMPREPLY=($(compgen -W "${arguments}" -- $cur))
		return 0;
	else
		opts=$(ls /usr/local/include/xbian-config/modules/);
		COMPREPLY=($(compgen -W "${opts}" -- ${cur}))
		return 0;
	fi
}
complete -F _xbian-config xbian-config
