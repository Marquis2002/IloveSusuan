def new(num_buckets = 256):
    """Initializes the Map with the given number of the buckets."""
    # aMap is a list
    aMap = []
    # here is a loop
    for i in range(0, num_buckets):
        # append the Bracket as the bucket
        aMap.append([])
    # every new() will return a list like [[], [], [],... , []], which have 256 buckets
    return aMap

def hash_key(aMap, key):
    # hash is a special value according to the given thing working as a key
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    # return like this will make the key no lager than len(aMap)
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    # decide which rank of the list aMap will be chosen
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    # every get_bucket(aMap, key) will return one position of aMap
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    # judge the key and (k, v), if key == k, then get v
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default(None if not set) when not found.
    """
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k,v = kv
        if key == k:
            # return in loop-body will break the system?
            return i, k ,v

    # default get_slot(aMap, key) is -1, key, default
    return -1, key, default

def get(aMap, key, default=None):
    # by using get_slot, this function will get value of the slot
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default = default)
    return v

# use set() to replace or append k,v in aMap
def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    # You can see we get the key positon bucket of the buckets list
    bucket = get_bucket(aMap, key)
    # then have i, k, v depending on the given bucket
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        # i was generated depending on the number of the buckets, and the default value is -1
        # if the key exists, then replace it
        bucket[i] = (key, value)
    else:
        # the key does not exist, append to create it
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)
    # xrange is not used in python3 but python 2
    for i in range(len(bucket)):
        # why not just bucket, cause bucket = aMap[bucket_id] in get_bucket
        # bucket[i] == aMap[bucket_id][i]
        # k,v = bucket[i], I don't think so
        k = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the map."""
    for bucket in aMap:
        # empty will be determined as false
        if bucket:
            for k, v in bucket:
                print(k, v)

def dump(aMap):
    """Copy the whole dict to save it"""
    bMap = new()
    i = 0
    for bucket in aMap:
        bMap[i] = bucket
        i = i + 1
    return bMap