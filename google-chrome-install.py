import sys, os

def main():
	print("\n1) Google-chrome-stable\n\n2) Google-chrome-beta\n\n3) Google-chrome-Dev\n\n0) Quit\n")
	inst = input("Choose version: ")

	if inst == "1":
		os.system('sh sh/chrome-stable.sh')
	elif inst == "2":
		os.system('sh sh/chrome-beta.sh')
	elif inst == "3":
		os.system('sh sh/chrome-dev.sh')
	elif inst == "0":
		print(' ')
	else:
		main()

main()