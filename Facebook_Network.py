import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    num_users = int(friends[0])
    for line in friends[1:]:
        user_id, friend_id = map(int, line.split())
        if user_id != friend_id: 
            friends_list = sorted([friend_id])
            if friend_id != user_id:
                network.append((user_id, friends_list))
    sorted_network = sorted(network, key=lambda x: (x[0], x[1]))
    user_friends = [[] for _ in range(num_users + 1)]
    for user_id, friends_list in sorted_network:
        user_friends[user_id].extend(sorted(friends_list))
        for friend_id in friends_list:
            if friend_id != user_id: 
                user_friends[friend_id].append(user_id)

    result = [(i, sorted(set(friends) - {i})) for i, friends in enumerate(user_friends) if friends]

    return result


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    index_user1 = next(i for i, user in enumerate(network) if user[0] == user1)
    index_user2 = next(i for i, user in enumerate(network) if user[0] == user2)
    friends_user1 = set(network[index_user1][1])
    friends_user2 = set(network[index_user2][1])
    common = sorted(list(friends_user1 & friends_user2))
    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    user_index = next((i for i, u in enumerate(network) if u[0] == user), None)

    if user_index is not None:
        user_friends = set(network[user_index][1])
        max_common_friends = 0
        recommended_friend = None

        for other_user_index, other_user_friends in enumerate(network):
            other_user_id, other_friends = other_user_friends
            if other_user_id != user and other_user_id not in user_friends:
                similar_friends = len(set(other_friends) & user_friends)
                if similar_friends > max_common_friends or (similar_friends == max_common_friends and other_user_id < recommended_friend):
                    max_common_friends = similar_friends
                    recommended_friend = other_user_id

        return recommended_friend
    return None
    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    count = 0
    for user_friends in network:
        friends = user_friends[1]
        if len(friends) >= k:
            count = count + 1
        else:
            None
    return count
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''

    max_friends = 0
    for user_friends in network:
        friends = user_friends[1] 
        num_friends = len(friends)
        if num_friends > max_friends:
            max_friends = num_friends
        else:
            None
    return max_friends
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]

    if not network:
        return max_friends

    # Calculate the number of friends for each user and store in max_friends list
    max_friends = [len(friends) for user_id, friends in network]

    # Find the maximum number of friends
    max_friends_count = max(max_friends)

    # Find the people with the maximum number of friends
    max_friends_ids = [user_id for user_id, count in enumerate(max_friends) if count == max_friends_count]

    return max_friends_ids


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''


    total_friends = sum(len(user[1]) for user in network)
    total_users = len(network)
    if total_users > 0:
        result= total_friends / total_users
    else:
        result = 0
    return result
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    for user_id, friend_list in network:
        all_other_users = {user[0] for user in network if user[0] != user_id}
        if set(friend_list) == all_other_users:
            return True
    return False

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    while True:
        user_id = int(input("Enter a user ID: "))
        if any(user_id == user[0] for user in network):
            return user_id
        else:
            print("User ID not found in the network. Please try again.")
    

##############################
# main


file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    

