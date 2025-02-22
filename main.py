from semu_fuzz import globs
from semu_fuzz.configuration import args, config
from semu_fuzz.emulate import uc, nvic
from semu_fuzz.log import debug, fuzz_stat
from semu_fuzz.emulate.semu.rule import rules_configure
from semu_fuzz.handlers import reset_func_handler
import gc

# for debug when haven't install this pkg.
# import sys
# import os
# sys.path.append(os.pos.path.dirname(__file__))

def main():
    global args, config, uc
    # configure args and config
    args = args.parse_args()
    config = config.parse_config()

    # configure uc
    uc = uc.uc_configure()
    
    # configure log
    if args.debug_level:
        debug.debug_configure()
    if args.stat:
        fuzz_stat.stat_configure()
    # print(globs.valid_block)

    # configure nvic
    if config.isr_vector >= 0x8000000:
        nvic.nvic_configure(uc, 256, 0x8000000)
    else:
        nvic.nvic_configure(uc, 256, 0x0)

    # configure handler
    if config.symbols != None:
        reset_func = config.handlers.keys()
        for addr, func_name in config.symbols.items():
            if func_name in reset_func:
                reset_func_handler(uc, addr, config.handlers[func_name])

    # configure rule
    rules_configure(uc, globs.config.rules)

    # Collect garbage once in order to avoid doing so while fuzzing
    gc.collect()

    # start emulation or fuzz
    emulate_mode = globs.config.emulate_mode
    if emulate_mode == 'emulate':
        from semu_fuzz.emulate.uc import uc_emulate
        uc_emulate(uc)
    elif emulate_mode == 'fuzz':
        from semu_fuzz.fuzz.fuzz import fuzz_emulate
        fuzz_emulate(uc)
    else:
        print("%s mode has not been supported, yet." % emulate_mode)

if __name__ == "__main__":
    main()