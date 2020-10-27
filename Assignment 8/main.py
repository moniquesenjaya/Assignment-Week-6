pokemon = 'audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'
pokemon_list = []
pokemon_dict = {}

# Split to a list
pokemon_list = pokemon.split()

# Split all pokemons into an actual dictionary with first letter as the key
for name in pokemon_list:
    if name[0] not in pokemon_dict:
         pokemon_dict[name[0]] = [name]
    else:
        pokemon_dict[name[0]].append(name)

def make_list(sequence):
    global longest_sequence

    # Longest checking
    longest_sequence = []
    if len(sequence) > len(longest_sequence):
        longest_sequence = sequence

    # Recursion to find the next pokemon of the sequence
    if sequence[-1][-1] in pokemon_dict:
        for name in pokemon_dict[sequence[-1][-1]]:
            if name not in sequence:
                sequence.append(name)
                make_list(sequence)

# Run through all possible combinations
for sequence in pokemon_list:
    make_list([sequence])

print(longest_sequence)


