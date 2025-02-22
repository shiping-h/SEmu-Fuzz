from .drl.transition_graph import TransitionGraph

args = None
config = None
uc = None
config_dir = ""
block_count = 0
user_input = []
tool_name = 'semu-fuzz'
# 统计基本块覆盖次数
visit_block_count = {}
valid_block = set()
# 状态转换图
transition_graph = TransitionGraph()
pre_node = None
reg_data = None

# 状态节点（执行的block集合）
state_blocks = []
state_node = None
# 动作边（输入的寄存器数据）
action_data = None

# 数据寄存器有效位数
data_widths = {}

# 处理中断
ISINTERRPUT = False
isr_state_blocks = []
isr_state_node = None
isr_action_data = None


#-- parameters in configuration --#
DEFAULT_BASIC_BLOCK_LIMIT = 30000000 # the number of basic blocks to be executed

#-- parameters in emulate --#
DEFAULT_NUM_NVIC_VECS = 240 # the number of irqs in nvic vtor
INTERRUPT_INTERVAL = 1500 # the number of interrupt interval blocks
DATA_REGS_INTERVAL = 1000 # the number of blocks for data register write interval
PAGE_SIZE = 0x1000 # the size of page