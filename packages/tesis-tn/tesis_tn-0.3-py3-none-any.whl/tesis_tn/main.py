import itertools
from math import ceil

def check_shifted_equal(list1, list2):
    if list1 == list2:
        return (True, 0)
    for i in range(len(list1)):
        temp1 = list2.copy()
        temp2 = list2.copy()
        temp1 = temp1[1:] + temp1[:1]
        temp2 = temp2[-1:] + temp2[:-1]
        if temp1 == list1:
            return (True, i+1)
        if temp2 == list1:
            return (True, -i-1)
    return (False, 0)

def is_shifted_version(arr1, arr2):
    # Check if arrays are of equal length
    if len(arr1) != len(arr2):
        return False
    
    # Double the first array
    doubled_arr1 = arr1 + arr1

    # Check if the second array is a "substring" of the doubled array
    return any(doubled_arr1[i:i + len(arr2)] == arr2 for i in range(len(arr1)))
    

def update_states_arbitrary(grid_row, rule_function, width, neighbour_radius = 1):
    '''
    this function will update the states of a row of a grid using a rule function
    
    Args:
        grid_row: row of the grid to update
        rule_function: rule function to update the states
        width: width of the row
        neighbour_radius: radius of the neighbourhood
    
    Returns:
        new_grid: updated row of the grid
    '''
    new_grid = [0] * width
    for cell in range(0, width):
        if cell+neighbour_radius+1 > width:
            neighbour = grid_row[cell-neighbour_radius:] + grid_row[:cell+neighbour_radius+1-width]
        elif cell-neighbour_radius < 0:
            neighbour = grid_row[width+cell-neighbour_radius:] + grid_row[:cell+neighbour_radius+1]
        else:
            neighbour = grid_row[cell-neighbour_radius:cell+neighbour_radius+1]
        new_grid[cell] = rule_function(neighbour)

    
    return new_grid



def generate_arrays(n, K):
    all_arrays = []
    
    for length in range(1, n + 1):
        for array in itertools.product(range(K), repeat=length):
            all_arrays.append(list(array))
    
    return all_arrays

def generate_unique_shift_invariant_arrays(n, K):
    '''
    this function will generate all unique shift invariant arrays of length n with K states
    
    Args:
        n: length of the arrays
        K: number of states
        
    Returns:
        unique_arrays: list of unique shift invariant arrays
    '''
    
    def is_shift_unique(array, existing_arrays):
        # Generate all circular shifts of the array
        circular_shifts = {tuple(array[i:] + array[:i]) for i in range(len(array))}
        # Check if any circular shift already exists
        return not any(shift in existing_arrays for shift in circular_shifts)
    

    unique_arrays = set()
    for length in range(1, n + 1):
        for array in itertools.product(range(K), repeat=length):
            if is_shift_unique(array, unique_arrays):
                #check that array is not a multiple of another array in the list
                skip = False
                for elem in unique_arrays:
                    if array*len(elem) == elem*len(array): #product will be the same if one is a multiple of the other
                        skip = True
                        break
                if skip:
                    continue


                unique_arrays.add(tuple(array))
    return [list(array) for array in unique_arrays]


def find_domains(rule, k_states, neighbour_radius, max_temporal_period = 4, max_spatial_period = 3):
    '''
    this function will find the domains of a rule
    
    Args:
        rule: rule function to update the states
        k_states: number of states
        neighbour_radius: radius of the neighbourhood
        max_temporal_period: maximum temporal period
        max_spatial_period: maximum spatial period
        
    Returns:
        domains: list of domains
    '''
    domains = []
    #all = generate_arrays(max_spatial_period, k_states)
    all = generate_unique_shift_invariant_arrays(max_spatial_period, k_states)
    all.sort(key=len)
    print("candidates: ", len(all))
    for candidate in all:
        temp = candidate.copy()
        temp *= 2*neighbour_radius + 1
        temp2 = temp.copy()
        past_configs_temp = []
        past_configs_temp.append(temp2)
        #iterate the candidate to see if it is a domain already in the list
        for i in range(max_temporal_period):
            temp2 = update_states_arbitrary(temp2, rule, len(temp2), neighbour_radius)
            past_configs_temp.append(temp2)
            bool_shift = is_shifted_version(temp, temp2)
            if bool_shift:
                domains.append(candidate)
                break

    return domains

def update_states_arbitrary_boundless(grid_row, rule_function, width, len_dom_i, len_dom_j, neighbour_radius = 1):
    '''
    this function will update the states of a row of a grid using a rule function

    Args:
        grid_row: row of the grid to update
        rule_function: rule function to update the states
        width: width of the row
        len_dom_i: length of the domain i
        len_dom_j: length of the domain j
        neighbour_radius: radius of the neighbourhood

    Returns:
        new_grid: updated row of the grid
    '''
    new_grid = [0] * width
    grid_temp = grid_row.copy()
    temp_i = grid_row[:len_dom_i] * (neighbour_radius)
    temp_j = grid_row[width-len_dom_j:] * (neighbour_radius)
    grid_temp = temp_i + grid_temp + temp_j

    for cell in range(0, width):
        temp = cell + len(temp_i)
        neighbour = grid_temp[temp-neighbour_radius:temp+neighbour_radius+1]
        new_grid[cell] = rule_function(neighbour)
            
    return new_grid


def is_subsequence(str1, str2):
    n, m = len(str1), len(str2)
    
    if m > n:
        return (False, 0)
    
    for i in range(n - m + 1):
        if str1[i:i + m] == str2:
            return (True, i)
    
    return (False, 0)

def find_particles(rule, domain_list, k_states, neighbour_radius, max_spatial_period = 4, max_temporal_period = 4, max_middle_length = 2, same_domain_particles = True, multiple_particles_per_pair = True):
    '''
    this function will take a list of domains and return the particles that can be generated from them

    Args:
        rule: rule function to update the states
        domain_list: list of domains
        k_states: number of states
        neighbour_radius: radius of the neighbourhood
        max_spatial_period: maximum spatial period
        max_temporal_period: maximum temporal period
        max_middle_length: maximum length of the middle element
        same_domain_particles: boolean to allow particles with the same domain on both ends
        multiple_particles_per_pair: boolean to allow multiple particles per pair of domains

    Returns:
        particles: list of particles with the following format (particle_id, domain_i, middle, domain_j, velocity, temporal_period)
    '''
    particles = []
    ID = 0
    generated = generate_arrays(max_middle_length, k_states)
    generated.insert(0, [])
    for domain_i in domain_list:
        for domain_j in domain_list:
            middle_elem = generated.copy()
            #comentar luego
            if domain_i == domain_j and same_domain_particles == False:
                continue
                
            for i in range(max_middle_length):
                if domain_i*(i+1) in middle_elem:
                    middle_elem.remove(domain_i*(i+1))
                if domain_j*(i+1) in middle_elem:
                    middle_elem.remove(domain_j*(i+1))

            
            next_bool = False 
            for aditional in middle_elem:
                #comentar luego
                if next_bool and multiple_particles_per_pair == False:
                    break
                if domain_i + aditional == domain_j or domain_i + domain_j == aditional:
                    continue

                domain_i_multiplier = 4*ceil((max_temporal_period)/len(domain_i)) * (2*neighbour_radius+1)
                domain_j_multiplier = 4*ceil((max_temporal_period)/len(domain_j)) * (2*neighbour_radius+1)

                temp = domain_i_multiplier*domain_i + aditional + domain_j_multiplier*domain_j

                check_template = temp[max_temporal_period*neighbour_radius:-max_temporal_period*neighbour_radius]#domain_i*(domain_i_multiplier//2) + aditional + domain_j*(domain_j_multiplier//2)

                temp2 = temp.copy()
                for j in range(max_temporal_period):
                    temp2 = update_states_arbitrary_boundless(temp2, rule, len(temp2), len(domain_i), len(domain_j), neighbour_radius)
                    
                    bool_shift, shift = is_subsequence(temp2, check_template)
                    if bool_shift:# and next_bool == False:
                        initial_shift = is_subsequence(temp, check_template)[1]
                        '''print("initial shift: ", initial_shift)
                        print("half", len(temp)//2 - len(domain_i)*(domain_i_multiplier//2) - len(aditional)//2) '''
                        
                        shift = shift - initial_shift

                        particle_to_add = (ID, domain_i, aditional, domain_j, shift, j+1, [])

                        particles.append(particle_to_add)
                        ID += 1
                        next_bool = True
                        break

    return particles

def particle_filter(states, particle_list):
    filtered_grid = []
    row_len = len(states[0])
    for row in states:
        filtered_row = [0]*row_len
        for particle in particle_list:
            id, domain_i, middle, domain_j, shift, temporal_period, decays = particle
            temp = domain_i*2 + middle + domain_j*2
            temp_2 = domain_i + middle + domain_j
            temp_len = len(temp)
            temp_len_2 = len(temp_2)
            d_i = len(domain_i)
            i=0
            while i <= row_len - temp_len:
                if row[i:i+temp_len] == temp:
                    for j in range(temp_len_2):
                        filtered_row[i+d_i+j] = 1
                    i += temp_len
                else:
                    i += 1
        filtered_grid.append(filtered_row)

    return filtered_grid



def domain_filter(states, domain_list):
    '''
    this function will take a grid of states and return a grid with the domains filtered out
    
    Args:
        states: grid of states
        domain_list: list of domains
    
    Returns:
        filtered_grid: grid with the domains filtered out
    '''
    filtered_grid = []

    for row in states:
        filtered_row = [1] * len(row)
        skip = 0
        
        for i in range(len(row)):
            if skip > 0:
                skip -= 1
                continue
            
            for domain in domain_list:
                domain_len = len(domain)
                if row[i:i + domain_len] == domain:
                    filtered_row[i:i + domain_len] = [0] * domain_len
                    skip = domain_len - 1
                    break
        
        filtered_grid.append(filtered_row)

    return filtered_grid


def describe_string_with_domains(s, templates, max_temporal_period):
    '''
    this function will take a string and return the domains that describe it

    Args:
        s: string to describe
        templates: list of domains
        max_temporal_period: maximum temporal period

    Returns:
        result: list of domains that describe the string
    '''
    
    result = []
    i = 0
    
    while i < len(s):
        max_match = max(
            (template for template in templates if s.startswith(template * 5, i)),#(2+ceil(max_temporal_period/len(template))), i)),
            key=len,
            default=""
        )
        
        if max_match:
            i += len(max_match) * (max_temporal_period +4)
            if not result or result[-1] != max_match:
                result.append(max_match)
        else:
            i += 1
            
    return result


def describe_string_with_particles(result, particle_list):
    '''
    this function will take a domain result and return the particles that describe it

    Args:
        result: list of domains
        particle_list: list of particles with the following format (particle_id, domain_i, middle, domain_j, velocity, temporal_period)

    Returns:
        particle_result: list of particles that describe the result
    '''
    particle_result = []
    i = 0
    while i+1 < len(result):
        temp_domain_i = result[i]
        temp_domain_j = result[i+1]
        #find which particle has domain_i and domain_j
        for particle in particle_list:
            id, domain_i, middle, domain_j, shift, temporal_period, decays = particle
            if ''.join(map(str, domain_i)) == temp_domain_i and ''.join(map(str, domain_j)) == temp_domain_j:
                particle_result.append(id)
                break
        i += 1

    return particle_result

def describe_configuration(domain_list, particle_list, configuration, max_middle_length):
    '''
    Args:
        domain_list: list of domains
        particle_list: list of particles with the following format (particle_id, domain_i, middle, domain_j, velocity, temporal_period)
        configuration: configuration to describe
        max_middle_length: maximum length of the middle element
        
    Returns:
        result: list of particles that describe the configuration
    '''
    temp_config = configuration.copy()
    temp_domain_list = domain_list.copy()
    #convert configuration to string
    temp_config = ''.join(map(str, temp_config))
    #convert each element of the domain list to string
    temp_domain_list = [''.join(map(str, x)) for x in temp_domain_list]
    result = describe_string_with_domains(temp_config, temp_domain_list, max_middle_length)

    return describe_string_with_particles(result, particle_list)

def find_interactions(domains, particles, rule, neighbour_radius, max_middle_length):
    '''
    Args:
        domains: list of domains
        particles: list of particles with the following format (particle_id, domain_i, middle, domain_j, velocity, temporal_period)
        rule: rule function to update the states
        neighbour_radius: radius of the neighbourhood
        max_middle_length: maximum length of the middle element
        
    Returns:
        interactions: dictionary with the interactions between particles
    '''
    interactions = {}
    if not particles:
        return interactions
    max_temporal_period_temp = max([x[5] for x in particles])
    for particle in particles:
        id, domain_i, middle, domain_j, shift, temporal_period, decays = particle


        for particle2 in particles:
            id2, domain_i2, middle2, domain_j2, shift2, temporal_period2, decays2 = particle2
            if domain_j != domain_i2:
                continue
            if shift/temporal_period <= shift2/temporal_period2:
                continue
            if decays2:
                continue

            temp_multiplier = 2*(2*neighbour_radius+1) * ceil((max_temporal_period_temp)/len(domain_i))#2*(2*neighbour_radius+1)*ceil((max_temporal_period_temp**2)/len(domain_i))
            temp2_multiplier = 2*(2*neighbour_radius+1) * ceil((max_temporal_period_temp)/len(domain_j2))#2*(2*neighbour_radius+1)*ceil((max_temporal_period_temp**2)/len(domain_j2))

            temp = domain_i * temp_multiplier + middle + domain_j * 2
            temp2 = domain_i2 * 2 + middle2 + domain_j2 * temp2_multiplier

            interaction_ca = temp + temp2
            for i in range(len(domain_j+domain_i2)*2+len(middle+middle2)):
                interaction_ca = update_states_arbitrary_boundless(interaction_ca, rule, len(interaction_ca), len(domain_i), len(domain_j2), neighbour_radius)

            
            interactions[(id, id2)] = [] 

            for i in range(2*max_temporal_period_temp):
                for check_particle in particles:
                    check_id, check_domain_i, check_middle, check_domain_j, check_shift, check_temporal_period, check_decays = check_particle
                    '''if check_id in interactions[(id, id2)]:
                        continue'''
                    if check_domain_i == domain_i and check_domain_j == domain_j2:
                        check_temp = check_domain_i * (2*ceil(max_middle_length/len(check_domain_i))) + check_middle + check_domain_j * (2*ceil(max_middle_length/len(check_domain_j)))
                        if is_subsequence(interaction_ca, check_temp)[0]:
                            if interactions[(id, id2)]:
                                if check_id not in interactions[(id, id2)]:
                                    interactions[(id, id2)].append(check_id)
                            else:
                                interactions[(id, id2)] = [check_id]
                            
                interaction_ca = update_states_arbitrary_boundless(interaction_ca, rule, len(interaction_ca), len(domain_i), len(domain_j2), neighbour_radius)

            if len(describe_string_with_domains(''.join(map(str, interaction_ca)), [''.join(map(str, x)) for x in domains], max_middle_length)) == 1 and domain_i != domain_j2:
                #print("anihilated")
                interactions[(id, id2)] = []

    
    return interactions



class Particle:
    def __init__(self, particle_type, initial_position, ready = True):
        self.type = particle_type[0]
        self.velocity = particle_type[1]
        self.position = initial_position
        self.ready = ready

    def __str__(self):
        return "Type: {}, Velocity: {}, Position: {}".format(self.type, self.velocity, self.position)
    
    def update_position(self, value):
        self.position = value

    def update_status(self):
        self.ready = not self.ready

def are_close(particle_a, particle_b):
    return particle_a.position + particle_a.velocity >= particle_b.position + particle_b.velocity and particle_b.position > particle_a.position


def update_state(instance, particle_types, particle_interactions, width, height):
    '''
    Args:
        instance: initial configuration of the particle configuration
        particle_types: list of particles with the following format (particle_id, velocity)
        particle_interactions: dictionary with the interactions between particles
        width: width of the particle configuration
        height: iteration to run the particle configuration

    Returns:
        new_instance: updated configuration of the particle configuration
    '''
    #create a new list of particles
    new_instance = []
    used_particles = []
    #for each particle, check all other particles to see if they are close
    #if they are close, check if they can interact
    #if they can interact, update the particles
    for i, particle in enumerate(instance):
        if particle in used_particles:
            continue

        if (particle.type, -1) in particle_interactions:
            #print("Particle is in particle_interactions")
            add = False
            result = particle_interactions[(particle.type, -1)]
            for i, new_particle in enumerate(result):
                new_instance.append(Particle(particle_types[new_particle], particle.position + i))#, False)
            continue

        add = True
        for j, other_particle in enumerate(instance[i+1:]):
            #print(particle, other_particle, "are close: ", are_close(particle, other_particle))
            '''
            if i == j:
                print("Same particle")
                continue'''
            if not other_particle.ready or other_particle in used_particles:
                #print("Other particle too new to colide or interacted in same iteration")
                continue
            
            if are_close(particle, other_particle):
                if (particle.type, other_particle.type) not in particle_interactions:
                    #print("No interaction between particles")
                    continue
                used_particles.append(particle)
                used_particles.append(other_particle)
                particle.update_status()
                other_particle.update_status()
                add = False
                result = particle_interactions[(particle.type, other_particle.type)]
                for i, new_particle in enumerate(result):
                    new_instance.append(Particle(particle_types[new_particle], particle.position + i))#, False))

        if add:
            particle.update_position((particle.position + particle.velocity) % width)
            new_instance.append(particle)


    return sorted(new_instance, key=lambda x: x.position) #new_instance




def create_particle_conf(conf_tuple_list, particle_list, interactions):
    '''
    Args:
        conf_tuple_list: list of tuples with the following format (particle_id, velocity, position)
        particle_list: list of particles with the following format (particle_id, domain_i, middle, domain_j, velocity, temporal_period)
        interactions: dictionary with the interactions between particles

    Returns:
        all_states_for_ploting: list of lists with the states of the particles at each iteration
        initial: list with the initial configuration of the CA that replicates the particles' emergent behavior
    '''

    standard_particle_list = [(particle[0], round(float(particle[4]/particle[5]),2)) for particle in particle_list]

    #type, velocity, position
    #conf_tuple_list = [(particle[0], particle[3], particle[1]) for particle in conf_tuple_list]

    instance_particle_list = []

    if len(conf_tuple_list) >1:
        width = max([particle[2] for particle in conf_tuple_list]) + 10
        #transform the width into an integer
        width = int(width)
    else:
        width = int(max([particle[2] for particle in conf_tuple_list])*2)

    height = width

    for particle in conf_tuple_list:
        instance_particle_list.append(Particle((particle[0], particle[1]), particle[2]))


    all_states_for_ploting = []

    for i in range(height - 1):
        all_states_for_ploting.append([-1] * width)
        for particle in instance_particle_list:
            all_states_for_ploting[i][int(round(particle.position))%width] = particle.type
        
        instance_particle_list = update_state(instance_particle_list, standard_particle_list, interactions, width, height)

    
    all_states = []
    progress = 0
    width = 0

    if len(conf_tuple_list)>1:
        
        initial = []
        i=1
        while i < len(conf_tuple_list)+1:
            p1_type, p1_velocity, p1_position = conf_tuple_list[i-1]
            p2_type, p2_velocity, p2_position = conf_tuple_list[i%len(conf_tuple_list)]

            particle_1 = particle_list[p1_type]
            particle_2 = particle_list[p2_type]

            '''if particle_1[3] != particle_2[1]:
                print("Invalid particle configuration")
                return
            else:'''
            domain_temp = particle_1[1]
            len_domain_temp = len(domain_temp)
            middle_elem_temp = particle_1[2]
            len_middle_elem_temp = len(middle_elem_temp)
            #fill until cell number conf_tuple_list[i-1][2]
            for j in range(ceil((p1_position - len(initial))/len_domain_temp)*len_domain_temp):
                #initial[progress + j] = domain_temp[j % len_domain_temp]
                initial.append(domain_temp[j % len_domain_temp])

            
            #progress = ceil(p1_position/len_domain_temp)*len_domain_temp

            if middle_elem_temp:
                print("Middle elem temp: ", middle_elem_temp)
                for j in range(len_middle_elem_temp):
                    #initial[progress + j] = middle_elem_temp[j]
                    initial.append(middle_elem_temp[j])

                
            #progress += len_middle_elem_temp

            if i == len(conf_tuple_list):
                domain_j_temp = particle_1[3]
                len_domain_j_temp = len(domain_j_temp)
                for j in range(5*len_domain_j_temp):
                    #initial[progress + j] = domain_j_temp[j % len_domain_temp]
                    initial.append(domain_j_temp[j % len_domain_j_temp])


        i += 1
    
    else:
        #only one particle
        particle = conf_tuple_list[0]
        particle_type, particle_velocity, particle_position = particle
        particle = particle_list[particle_type]
        domain_i_temp = particle[1]
        len_domain_i_temp = len(domain_i_temp)
        middle_elem_temp = particle[2]
        len_middle_elem_temp = len(middle_elem_temp)
        domain_j_temp = particle[3]
        len_domain_j_temp = len(domain_j_temp)

        #width = ceil(particle_position/len_domain_i_temp)*len_domain_i_temp + len_middle_elem_temp + ceil(particle_position/len_domain_j_temp)*len_domain_j_temp
        initial = []

        
        '''if domain_i_temp != domain_j_temp:
            print("Invalid particle configuration")
            return
        else:'''
        for i in range(ceil(particle_position/len_domain_i_temp)*len_domain_i_temp):
            #initial[i] = domain_i_temp[i % len_domain_i_temp]
            initial.append(domain_i_temp[i % len_domain_i_temp])

        progress = ceil(particle_position/len_domain_i_temp)*len_domain_i_temp

        if middle_elem_temp:
            for i in range(len_middle_elem_temp):
                #initial[progress + i] = middle_elem_temp[i]
                initial.append(middle_elem_temp[i])

        progress += len_middle_elem_temp
        

        for i in range(ceil(particle_position/len_domain_j_temp)*len_domain_j_temp):
            #initial[progress + i] = domain_j_temp[i % len_domain_j_temp]
            initial.append(domain_j_temp[i % len_domain_j_temp])



    return all_states_for_ploting, initial
