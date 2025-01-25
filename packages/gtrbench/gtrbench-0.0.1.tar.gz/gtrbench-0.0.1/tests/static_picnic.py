from gtrbench.picnic.static_picnic.base import StaticGoingOnAPicnic

# Get a new object for the static picnic game
static_picnic_obj = StaticGoingOnAPicnic(
    difficulty='L1',
    num_init_examples=2
)

# Create a new game instance
static_picnic_obj.create_game_instance()

# Request more examples
static_picnic_obj.get_more_examples(n=1)
static_picnic_obj.get_more_examples(n=2)
static_picnic_obj.get_more_examples(n=3)

# Validate guess
static_picnic_obj.validate_guess(guess='Items from the category kitchen appliances')

# Get game summary
static_picnic_obj.get_game_summary()

