# @author Riley Keane
# @since 20/3/18
# @modified 20/3/18

	.data
	
	.text
main: 	# allocating locals var
	# freq_count -20($fp)
	# item -16($fp)
	# i -12($fp)
	# list_length -8($fp)
	# the_list -4($fp)
	add $fp, $0, $sp
	addi $sp, $sp, -20
	
	# calling read_list
	jal read_list
	# svaing resturn value into -4($fp)
	sw $v0, -4($fp)

	# calling bubble_sort
	addi $sp, $sp, -4
	lw $t0, -4($fp)
	sw $t0, 0($sp)
	# calling
	jal bubble_sort
	# clearing arg off stack
	addi $sp, $sp, 4
	
	# list_length = len(the_list)
	lw $t0, -4($fp) #the_list
	lw $t0, 0($t0)
	sw $t0, -8($fp)
	
	# i = 0
	sw $0, -12($fp)
	
while:
	# while i < list_length
	lw $t0, -12($fp) # i
	lw $t1, -8($fp) # list_length
	slt $t0, $t0, $t1
	beq $t0, $0, end_while
	
	# item = the_list[i]
	lw $t0, -4($fp) # the_list
	lw $t1, -12($fp) # i
	sll $t1, $t1, 2
	add $t0, $t0, $t1
	lw $t0, 4($t0) # the_list[i]
	sw $t0, -16($fp)
	
	# freq_count = frequency(item, the_list)
	# pushing args to the stack
	lw $t0, -4($fp) # the_list
	lw $t1, -16($fp) #item
	addi $sp, $sp, -8
	sw $t0, 0($sp)
	sw $t1, 4($sp)
	# calling function
	jal frequency
	
	# returning from frequency function
	# clearing args
	addi $sp, $sp, 8
	# storing return in freq_count
	sw $v0, -20($fp)
	
	# i = i + freq_count
	lw $t0, -12($fp) # i
	lw $t1, -20($fp) # freq_count
	# i + freq_count
	add $t0, $t0, $t1
	sw $t0, -12($fp)
	
	# loop through while again
	j while
	
end_while:
	# exiting program
	addi $v0, $0, 10
	syscall

		
# read_list() function	
read_list: 
	.data
	prompt: .asciiz "How many days in the month?: "
	temp:	.asciiz "Enter a recorded temperature: "
	
	.text
	# saving $ra and $fp	
	addi $sp, $sp -8
	sw $ra, 4($sp)
	sw $fp, 0($sp)
	
	# copy $sp to $fp
	addi $fp, $sp, 0
	
	# allcoating space for locals
	# days
	# the_list
	# i
	# temp
	add $fp, $0, $sp
	addi $sp, $sp, -16

	# input("How many days in the month?: ")
	# printing prompt
	addi $v0, $0, 4
	la $a0, prompt
	syscall
	# getting input
	addi $v0, $0, 5
	syscall
	sw $v0, -16($fp) # days stored in -12($fp)
	
	# the_list = [None] * days
	lw $t0, -16($fp) # $t0 = days
	addi $t0, $0, 4  # days + 4
	addi $v0, $0, 9
	add $a0, $0, $t0 # setting array length to days + 4
	syscall
	sw $v0, -12($fp)
	# setting first array element to its length
	lw $t0, -16($fp)
	sw $t0, ($v0) # length is days 
	
	# i = 0
	lw $0, -8($fp)
	
	
read_list_loop: 
	# while i < days	
	lw $t0, -8($fp) # i
	lw $t1, -16($fp) # days
	slt $t0, $t0, $t1
	beq $t0, $0, end_read_list
	
	# temp = input('Enter a recorded temperature: ')
	# prompting user
	addi $v0, $0, 4
	la $a0, temp
	syscall
	# getting value
	addi $v0, $0, 5
	syscall
	sw $v0, -4($fp)	# stroing inputed temp
	
	# the_list[i] = temp
	lw $t0, -12($fp) # the_list
	lw $t1, -8($fp) # i
	lw $t2, -4($fp) # temp
	sll $t1, $t1, 2
	add $t0, $t0, $t1
	sw $t2, 4($t0)
	
	# i = i + 1
	lw $t0, -8($fp)
	addi $t0, $t0, 1
	sw $t0, -8($fp)
	
	j read_list_loop
	
end_read_list: 
	# load the_list into $v0	
	lw $v0, -12($fp)
	
	# dealocating local vars
	addi $sp, $sp, 16
	
	# restore $fp and $ra
	lw $fp, 0($sp)
	lw $ra, 4($sp)
	addi $sp, $sp, 8
	
	# jumping out of function
	jr $ra
# END READ_LIST FUNCTION


# Frequency(item, the_list) function	
frequency:
	.data 
appears: .asciiz " appears "
times:   .asciiz " times"
n:	 .asciiz "\n"
	
	.text
	# saving $fp and $ra on the stack
	addi $sp, $sp, -8
	sw $fp, 0($sp)
	sw $ra, 4($sp)
	
	# allocating space for local vars
	# list_length
	# i
	# item_count
	add $fp, $0, $sp
	addi $sp, $sp, -12
	
	# list_length = len(the_list)
	lw $t0, 8($fp)	# the_list
	lw $t1, 0($t0)
	sw $t1, -12($fp)
	
	# i = 0
	sw $0, -8($fp)
	# item_count = 0
	sw $0, -4($fp)
	
loop_freq:
	# while i < list_length
	lw $t0, -8($fp) # i
	lw $t1, -12($fp) # list_length
	slt $t0, $t0, $t1
	beq $0, $t0, end_loop_freq
	
	# if list[i] == item
	# getting list[i]
	lw $t0, -8($fp) # i
	lw $t1, 8($fp) # the_list
	sll $t0, $t0, 2
	add $t1, $t1, $t0
	lw $t0, 4($t1) # list[i]
	lw $t1, 12($fp) # item
	# comparrison
	bne $t0, $t1, end_if_freq
	
	# item_count = item_count + 1
	lw $t0, -4($fp) # item_count
	addi $t0, $t0, 1
	sw $t0, -4($fp)
	
	# i = i + 1
	lw $t0, -8($fp)
	addi $t0, $t0, 1
	sw $t0, -8($fp)
	
	j loop_freq
	
end_if_freq:
	# i = i + 1
	lw $t0, -8($fp)
	addi $t0, $t0, 1
	sw $t0, -8($fp)
	
	j loop_freq
	
end_loop_freq:
	# printing the result
	# "{item} appears {item_count} times"	
	# printing item
	addi $v0, $0, 1
	lw $a0, 12($fp)
	syscall
	# printing ' appears '
	addi $v0, $0, 4
	la $a0, appears
	syscall
	# printing item_count
	addi $v0, $0, 1
	lw $a0, -4($fp)
	syscall
	# printing ' times'
	addi $v0, $0, 4
	la $a0, times
	syscall
	# printing a new line
	addi $v0, $0, 4
	la $a0, n
	syscall
	
	# returning item_count
	lw $v0, -4($fp)
	
	# clearing local vars
	addi $sp, $sp, 12
	
	# restoring ra and fp
	lw $fp, 0($sp)
	lw $ra, 4($sp)
	addi $sp, $sp, 8
	
	jr $ra	
# END FREQUENCY FUNCTION


# bubble_sort(the_list) function
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
# END BUBBLE_SORT FUNCTION
	
