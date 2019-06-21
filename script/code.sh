#!/bin/bash

KEYID="E8D3009C6341BDEAF038009685AB6867E2147DDA"

encode() {
    (($# == 1)) || return 1
    local filename="$1"
    gpg --encrypt --armor --recipient $KEYID "$filename"
    return $?
}

decode() {
    (($# == 1)) || return 1
    local filename="$1"
    gpg "$filename"
    return $?
}
