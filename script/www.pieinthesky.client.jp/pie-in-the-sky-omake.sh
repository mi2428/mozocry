#!/bin/bash
cd $(dirname $0)

BASE_URL="http://www.pieinthesky.client.jp/"
CHAPTER_LIST=("trumprummy")

INTERVAL="0.2"
SAVE="./pie-in-the-sky-omake"

__chapter_downloader() {
    (($# == 1)) || return 1
    local chapter="$1"
    local n=1
    local folder="$SAVE/$chapter"
    mkdir -p $folder
    while true; do
        local wn=$(printf "%03d" "$n")
        local remote_path="$BASE_URL/$chapter/$wn.jpg"
        local local_path="$folder/$wn.jpg"
        wget -nv "$remote_path" -O "$local_path"
        (($? == 0)) || {
            rm "$local_path"
            break
        }
        [[ -n "$INTERVAL" ]] && sleep "$INTERVAL"
        n=$(($n + 1))
    done
    return 0
}

archive() {
    for chapter in ${CHAPTER_LIST[@]}; do
        __chapter_downloader $chapter &
    done
    wait
    zip -q -r "${SAVE}.zip" "$SAVE"
    rm -r "$SAVE"
    return 0
}

main() {
    for opt in "$@"; do
        case "$opt" in
            '--debug')
                set -x
                shift ;;
            '--save-dir')
                SAVE="$2"
                shift 2 ;;
        esac
    done
    archive
}

main $@
