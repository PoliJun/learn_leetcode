class Solution:
    '''
    use stack
    input: asteroids[1:n]
    output: collision: List[int]
    -----
    
    curr_direction = 0
    collision_list = [] 
    last_num = 0
    traverse the list from left to right:
      
      curr_direction = 0
      if num < 0:
        curr_direction = -1
      else:
        curr_direction = 1
      if last_direction + curr_direction == 0:
        if num + last_num != 0:
          collision_list.pop()
          collision_list.append(max(abs(num),abs(last_num)))
        else:
          collision_list.pop()
      else:
        collision.append(num)
      last_direction = curr_direction
      last_num = num
    return collision_list
      
    '''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      n = len(asteroids)
      last_direction = abs(asteroids[0]) / asteroids[0]
      last_num = asteroids[0]
      collision_list = [asteroids[0]]
      i = 1
      while i < n:
        curr_direction = 0
        if asteroids[i] < 0:
          curr_direction = -1
        else:
          curr_direction = 1
        if last_direction + curr_direction == 0:
          collision_list.pop()
          if last_num - asteroids[i] > 0 :
            if max(abs(last_num), abs(asteroids[i])) == abs(last_num):
              collision_list.append(last_num)
            else:
              collision_list.append(asteroids[i])
          last_direction = 0
          last_num = 0
        else:
          collision_list.append(asteroids[i])
          last_direction = curr_direction
          last_num = asteroids[i]
        i += 1
      return collision_list
            
        
        
