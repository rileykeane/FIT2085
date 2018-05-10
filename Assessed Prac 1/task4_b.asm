# @author Riley Keane
# @since 20/3/18
# @modified 20/3/18

	.data
	
	.text
bubble_sort:
	# saving $ra and $fp
	addi $sp, $sp, -8
	sw $ra, 4($sp)
	sw $fp, 0($sp)
	
	# set $fp to $sp
	add $fp, $0, $sp
	
	# creating space for locals 
	# sorted -16($fp)
	# list_length -12($fp)
	# i -8($fp)
	# temp -4($fp)
	addi $sp, $sp, -16
	
	# sorted = false (0)
	sw $0, -16($fp)

bubble_while1:	
	# while not sorted (sorted = 0)
	lw $t0, -16($fp)
	bne $t0, $0, end_bubble_while1
	
	# list_length = len(the_list)
	lw $t0, 8($fp) # the_list
	lw $t0, 0($t0)	
	sw $t0, -12($fp)
	
	# i = 0
	sw $0, -8($fp)
	
	# sorted = true
	addi $t0, $0, 1
	sw $t0, -16($fp)
	
bubble_while2:
	# i < list_length - 1
	lw $t0, -8($fp) # i
	lw $t1, -12($fp) # list_length
	addi $t1, $t1, -1 # list_length - 1
	slt $t0, $t0, $t1
	beq $t0, $0, end_bubble_while2
	
	# if the_list[i] > the_list[i+1]
	lw $t0, 8($fp)
	lw $t1, -8($fp) # i
	sll $t1, $t1, 2
	add $t0, $t0, $t1
	lw $t2, 4($t0) # the_list[i]
	lw $t3, 8($t0) # the_list[i+1]
	# comparrison 
	slt $t0, $t3, $t2
	beq $t0, $0, end_bubble_if
	
	# swapping values 
	# temp = the_list[i]
	lw $t0, 8($fp) # the List
	lw $t1, -8($fp) # i
	sll $t1, $t1, 2
	add $t0, $t0, $t1
	lw $t0, 4($t0) # the_list[i]
	# storing in temp
	sw $t0, -4($fp)
	
	# the_list[i] = the_list[i+1]
	lw $t0, 8($fp) # the_list
	lw $t1, -8($fp) # i
	sll $t1, $t1, 2
	add $t0, $t0, $t1
	lw $t1, 8($t0) # the_list[i + 1]
	sw $t1, 4($t0) # store $t0 into the_list[i]
	
	# the_list[i + 1] = temp
	lw $t0, 8($fp) # the_list
	lw $t1, -4($fp) # temp
	lw $t2, -8($fp) # i
	# i = i + 1
	addi $t2, $t2, 1
	sll $t2, $t2, 2
	add $t0, $t0, $t2
	sw $t1, 4($t0) # storing the value from temp into the_list[i+1]
	
	# sorted = False
	sw $0, -16($fp)
	
	# i = i + 1
	lw $t0, -8($fp)
	addi $t0, $t0, 1
	sw $t0, -8($fp)
	
	# looping through inner loop again
	j bubble_while2
	
end_bubble_if:
	# i = i + 1
	lw $t0, -8($fp)
	addi $t0, $t0, 1
	sw $t0, -8($fp)
	
	# looping through inner loop again
	j bubble_while2
	
end_bubble_while2:
	# looping through outer loop again
	j bubble_while1
	
end_bubble_while1:
	# return the_list
	lw $v0, 8($fp)
	
	# clearing local vars
	addi $sp, $sp, 16
	
	# restore $fp and $ra
	lw $fp, 0($sp)
	lw $ra, 4($sp)
	
	# jumping backing into caller
	jr $ra
	