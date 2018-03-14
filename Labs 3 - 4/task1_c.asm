# @author Riley Keane
# @since 12/3/18
# @modified 14/3/18

.data
	prompt:		.asciiz "Enter a year: "
	leap:		.asciiz "Is a leap year"
	notLeap: 	.asciiz "Not a leap year"
	newLine: 	.asciiz "\n"

.text
main:	# Creating space for one variable on the stack
	addi $fp, $sp, 0
	addi $sp, $sp, -4

	# printing the prompt
	addi $v0, $0, 4
	la $a0, prompt
	syscall
	
	# Getting user input for year
	addi $v0, $0, 5
	syscall
	sw $v0, -4($fp)		# storing year on the stack, year = -4($fp)
	
	# if year % 4 == 0
	lw $t0, -4($fp) 	# $t0 = year
	addi $t1, $0, 4		# $t1 = 4
	# year % 4
	div $t0, $t1
	mfhi $t1		# $t1 = year % 4
	# comparrison
	bne $0, $t1, else_1
	
	# if year % 100 == 0
	lw $t0, -4($fp)		# $t0 = year
	addi $t1, $0, 100 	# $t1 = 100
	# year % 100
	div $t0, $t1
	mfhi $t1		# $t1 = year % 100
	# comparrison
	bne $0, $t1, else_2
	
	# if year % 400 == 0
	lw $t0, -4($fp) 	# $t0 = year
	addi $t1, $0, 400	# $t1 = 400
	# year % 400
	div $t0, $t1
	mfhi $t1 		# $t1 = year % 100
	# comparrison
	bne $0, $t1, else_3
	
	# printing is a leap year
	addi $v0, $0, 4
	la $a0, leap
	syscall
	j endif
	
else_1: # if year % 4 != 0
	addi $v0, $0, 4
	la $a0, notLeap
	syscall			# printing is not a leap year
	j endif

else_2: # if year % 100 != 0 
	addi $v0, $0, 4
	la $a0, leap
	syscall			# printing a leap year
	j endif

else_3: # if year % 400 != 0
	addi $v0, $0, 4
	la $a0, notLeap		
	syscall			# printing is not a leap year
	
endif: 	# dealocting varaibles 
	addi $sp, $sp, 4
	addi $v0, $0, 10
	syscall			# ending 
	
	