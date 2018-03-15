# @author Riley Keane
# @since 11/3/18
# @modified 14/3/18

	.data
prompt: .asciiz "How many days in the month?: "
temp:	.asciiz "Enter a recorded temperature: "
	
	.text

main: 	# allocating local vars
	# the_list
	# max_temp
	addi $fp, $sp, 0
	addi $sp, $sp, -8
	
	# the_list = read_list()
	# Calling read list function
	jal read_list
	# saving return value from read_list
	sw $v0, -4($fp)	
	
	# dealocating variables 
	addi $sp, $sp, 4
	
	# max_temp = max(the_list)
	lw $t0, -4($fp) # the _list
	sw $t0, 0($sp) # arg 1
	# calling function
	jal max
	
	# clearing arg
	addi $sp, $sp, 4
	
	# storing result 
	sw $v0, -8($fp)
	
	lw $t0, -8($fp)
	
	# exit
	addi $v0, $0, 10
	syscall
	
	
read_list: 
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
	
	# while i < days
read_list_loop: 	
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
	

max: 	# saving $fp and $ra
	addi $sp, $sp, -8
	sw $fp, 0($sp)
	sw $ra, 4($sp)
	
	# copy $sp to $fp
	add $fp, $0, $sp
	
	# allocating local var
	# current_max
	# list_length
	# i
	addi $sp, $sp, -12
	
	# list_length = len(the_list)
	lw $t0, 8($fp)
	lw $t1, 0($t0)
	sw $t1, -8($fp)
	
	# current_max = the_list[0]
	lw $t0, 8($fp)
	lw $t0, 4($t0)
	sw $t0, -4($fp)
	
	# i = 1
	addi $t0, $0, 1
	sw $t0, -12($fp)
	
loop_max:	
	# while i < list_length
	lw $t0, -8($fp) # list_length
	lw $t1, -12($fp) # i
	slt $t0, $t1, $t0
	beq $t0, $0, end_max_loop
	
	# if current_max < the_list[i]
	lw $t0, -4($fp) # current_max
	lw $t1, 8($fp) # the_list
	lw $t2, -12($fp) # i
	sll $t2, $t2, 2
	add $t1, $t1, $t2
	lw $t1, 4($t1) # the_list[i]
	
	slt $t0, $t0, $t1
	beq $0, $t0, end_max_if
	
	# current_max = list[i]
	sw $t1, -4($fp) 
	
	# i = i + 1
	lw $t0, -12($fp) # i
	addi $t0, $t0, 1
	sw $t0, -12($fp)
	
	j loop_max
	
end_max_if:
	# i = i + 1
	lw $t0, -12($fp) # i
	addi $t0, $t0, 1
	sw $t0, -12($fp)
	
	j loop_max

end_max_loop:
	# setting $v0 to return value
	lw $v0, -4($fp)
	
	# claering local vars
	addi $sp, $sp, 12
	
	# restoring $ra and $fp
	lw $fp, 0($sp)
	lw $ra, 4($sp)
	addi $sp, $sp, 8
	
	# jump out of function
	jr $ra
	
	
	
	
	
	
	
	  
	
	

	

	
	
	
	

