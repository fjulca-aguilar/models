import subprocess
import sys
import os
if __name__ == "__main__":
	files = ['UN_128_em_1000', 'UN_129_em_1048', 'UN_132_em_1108', 'UN_134_em_1148', 'UN_452_em_642', 'UN_453_em_651', 'UN_465_em_954']
	files_dir = sys.argv[1]
	extension = sys.argv[2]
	cp = ['cp', '', '']
	replacelt = ['sed', '-i', '-e', 's/&lt;/\\\lt/g', '']
	replacegt = ['sed', '-i', '-e', 's/&gt;/\\\gt/g', '']
	replacelt2 = ['sed', '-i', '-e', 's/><</>\\\lt</g', '']
	replacegt2 = ['sed', '-i', '-e', 's/>></>\\\gt</g', '']
	for a_file in files:
		print(a_file)

		replacelt[4] = os.path.join(files_dir, a_file + extension)
		replacegt[4] = os.path.join(files_dir, a_file + extension)
		replacelt2[4] = os.path.join(files_dir, a_file + extension)
		replacegt2[4] = os.path.join(files_dir, a_file + extension)
		# print(replacelt)
		cp[1] = os.path.join(files_dir, a_file + extension)
		cp[2] = os.path.join(files_dir, a_file + extension + '.tmp')
		subprocess.call(cp)
		subprocess.call(replacelt)
		subprocess.call(replacegt)
		subprocess.call(replacelt2)
		subprocess.call(replacegt2)


