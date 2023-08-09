#! /usr/bin/env bash

set -e

PENSIEVE_ROOT=~/pensieve


function touch_everything() {
    cd "$PENSIEVE_ROOT"
    fd note.md --exec touch {}
}


function build_note() {
    # $1: path
    local path=$1
    cd "$path" || exit
    # if note.html already exists and its modification time is after
    # the modification time of note.md, skip
    if [[ -f "note.html" ]]; then
        if [[ "note.html" -nt "note.md" ]]; then
            echo "Skipping $path"
            return
        fi
    fi
    echo "Building $path"
    pensievetool render "note.md" > "note.html"
}

function build_directory() {
    for dir in ~/pensieve/"$1"/*; do
        # if `dir` is a directory
        if [[ -d $dir ]]; then
            build_note "$dir"
        fi
        cd "$PENSIEVE_ROOT" || exit
    done
}

touch_everything
build_directory "topic"
build_directory "thought"
build_directory "journal"
build_directory "project"
