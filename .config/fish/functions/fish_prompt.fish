# Defined in /tmp/fish.XvLjqW/fish_prompt.fish @ line 2
function fish_prompt
    switch "$fish_key_bindings"
        case fish_hybrid_key_bindings fish_vi_key_bindings
            set keymap "$fish_bind_mode"
        case '*'
            set keymap insert
    end
    set -l exit_code $status
    # Account for changes in variable name between v2.7 and v3.0
    set -l starship_duration "$CMD_DURATION$cmd_duration"
    "/usr/bin/starship" prompt --status=$exit_code --keymap=$keymap --cmd-duration=$starship_duration --jobs=(count (jobs -p))

    if set -q VIRTUAL_ENV
        echo -n -s (set_color -b blue white) "(" (basename "$VIRTUAL_ENV") ")" (set_color normal) " "
    end
end
