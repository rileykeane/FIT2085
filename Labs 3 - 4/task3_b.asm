# @author Riley Keane
# @since 16/3/18
# @modified 16/3/18

	.data
freq_count_prompt: .asciiz "Enter a value you would like the frequency of: "
	
	.text
main: 	# allocating local vars
	# the_list
	# count_temp
	add $fp, $0, $sp
	addi $sp, $sp, -8
	
	# the_list = raed_list()
	jal read_list
	# saving return value
	sw $v0, -8($fp)
	
	# getting count_temp from user
	# prinring prompt
	addi $v0, $0, 4
	la $a0, freq_count_prompt
	syscall
	# getting value
	addi $v0, $0, 5
	syscall
	sw $v0, -4($fp)
	
	# Calling frequency(count_temp, the_list)
	# passing arguments 
	# the_list
	# count_temp
	addi $sp, $sp, -8
	# arg 1 = the_list
	lw $t0, -8($fp)
	sw $t0, 0($sp)
	# arg 2 = count_temp
	lw $t1, -4($fp)
	sw $t1, 4($sp)
	# calling function 
	jal frequency
	# clearing args
	addi $sp, $sp, 8
	
	# exit
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
	lw $t0, -12($fp)
	lw $t1, -8($fp)
	lw $t2, -4($fp)
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
	
