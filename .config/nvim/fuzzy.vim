let g:ctrlp_working_path_mode = 'ra'

let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'

let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']
