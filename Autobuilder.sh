#!/bin/bash

export BASEPATH=/mnt/src/apt-web/web
rm -f $XBIANROOT/.to.run.apt.update

####for f in $(find -L ./ -maxdepth 4 -type d -name working); do [ -e $f/.git ] || continue; ( cd $f; echo $f; git ls-remote -h $(grep url .git/config | awk -F'=' '{print $2}') $(git branch|awk '{print $2}'); ); done

. $XBIANROOT/common.functions

for d1 in $(find -L ./ -mindepth 2 -maxdepth 2 -type d -name build); do
(
    cd $d1
    echo $d1 | grep -q ^'./WIP' && continue

    sharem=$(git ls-remote 2>/dev/null| grep HEAD |awk '{print $1}')
    shaloc=$(git log -n1 --format=oneline | awk '{print $1}')
    [ $sharem = $shaloc ] || printf ">>>>>>>>>>>>>>>\nxbian repo updated for %s\n>>>>>>>>>>>>>>>\n" $(dirname $d1)

    for d2 in $(find ./ -mindepth 2 -maxdepth 2 -type f -name config); do
    (
        cd $(dirname $d2)
        [ -e ../config ] && rexp ../config
        rexp config
        [ -z "$config_source_addr" -o -z "$config_source_branch" ] && continue
        [ ! -d working ] && continue

        cd working
        [ -e .force.skip ] && continue
        sharem=$(git ls-remote -h $config_source_addr $config_source_branch|awk '{print $1}')
        shaloc=$(git log -n1 --format=oneline | awk '{print $1}')
        [ $sharem = $shaloc -a ! -f .force -a ! -f .force.aptonly ] && continue
        [ ! -d $BASEPATH/$config_apt_dir ] && { echo "Error: TARGET not existend $BASEPATH/$config_apt_dir for $(basename $(dirname $d2)) at $(dirname $d1)"; continue; }

        echo "$(basename $(dirname $d2)) at $(dirname $d1)"
        [ -e ../config_aptdir ] && rexp ../config_aptdir
        if [ -n "$config_apt_dir" ]; then
            printf "BUILDING them: $sharem us: $shaloc\n----------------------------\n"
            [ -e .force.aptonly ] || ( cd "$XBIANROOT/$(dirname $d1)"; $xbiangit -m $(basename $(dirname $d2)); )
            rm -f .force; rm -f .force.aptonly
            if [ "$config_apt_rmold" = yes ]; then
                sudo su web1 -c "rm -v $BASEPATH/$config_apt_dir/$config_deb_pkgname*.deb"
            fi
            sudo su web1 -c "cp -v ../$config_deb_pkgname*.deb $BASEPATH/$config_apt_dir"
            echo "$BASEPATH/$config_apt_dir" >> $XBIANROOT/.to.run.apt.update
        else
            cd ..
            printf "EDIT: $(readlink -f ./)/config\n----------------------------\n"
        fi
    )
    done

)
done

exit 0

set -e
if [ -e $XBIANROOT/.to.run.apt.update ]; then
    apttoupdate=$(cat $XBIANROOT/.to.run.apt.update|sort|uniq)
    for u in $apttoupdate; do
        echo "UPDATING APT: $u"
        sudo su web1 -l -c "cd $u; ./update.sh"
    done
fi

rm -f $XBIANROOT/.to.run.apt.update
