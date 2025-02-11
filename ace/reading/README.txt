.data 
  
ascii db 35 dup('x')

.code 
main proc 
    lea ebx, ascii
    mov eax, 'A'
    mov [ebx], al
    mov ecx, 'B'
    mov [ebx+1], cl
    mov edx, 'C'
    mov [ebx+1], dl
    mov [ebx+2], dl
    mov [ebx+3], dl
    xor eax, eax      
    mov edx, 'T'
    mov eax, 'E'
    mov [ebx+4], al
    mov [ebx+2], al
    mov eax, 'F'
    mov [ebx+5], al
    add ebx, 5
    mov [ebx], al
    mov [ebx-1], dl
    mov eax, 123
    mov [ebx+1], al
    xor eax, eax
    add ebx, 15
    mov eax, 'l'
    mov [ebx], al
    mov eax, 34h
    mov [ebx-1], al
    sub al, 1
    mov [ebx-2],al 
    mov eax, 'r'
    mov [ebx-3], al
    sub ebx, 13
    mov ecx, 'y'
    mov [ebx], cl
    mov ecx, 48
    mov [ebx+1], cl
    mov ecx, 'u'
    mov [ebx+2], cl
    mov ecx, '_'
    mov [ebx+3], cl
    mov ecx, 52
    mov [ebx+4], cl
    mov ecx, 'r'
    mov [ebx+5], cl
    mov ecx, 51
    mov [ebx+6], cl
    mov ecx, '_'
    mov [ebx+7], cl
    mov ecx, 52
    mov [ebx+8], cl
    mov ecx, '_'
    mov [ebx+9], cl
    xor ebx, ebx
    xor eax, eax
    lea eax, ascii
    add eax, 20
    mov edx, 'x'
    mov ecx, "'"
    xor cl, dl
    mov [eax+1], cl
    mov ecx, 'L'
    xor cl, dl
    mov [eax+2], cl
    mov ecx, 11
    xor cl, dl
    mov [eax+3], cl
    mov ecx, 'M'
    xor cl, dl
    mov [eax+4], cl
    mov ecx, 'K'
    xor cl, dl
    mov [eax+5], cl
    mov ecx, 15h
    xor cl, dl
    mov [eax+6], cl
    mov ecx, 1ah
    xor cl, dl
    mov [eax+7], cl
    mov ecx, 14h
    xor cl, dl
    mov [eax+8], cl
    mov ecx, 01h
    xor cl, dl
    mov [eax+9], cl
    mov ecx, 27h
    xor cl, dl
    mov [eax+10], cl
    mov ecx, 'L'
    xor cl, dl
    mov [eax+11], cl
    mov ecx, 1bh
    xor cl, dl
    mov [eax+12], cl   
    mov ecx, 4bh
    xor cl, dl
    mov [eax+13], cl
    mov ecx, 5
    xor cl, dl
    mov [eax+14], cl
    mov [eax+14], dl
    add ebx, 12
    mov [eax + 1], dl
    add ebx, 'H'
    mov [eax + 2], dl
    add ebx, 3Fh
    mov [eax + 3], dl
    add ebx, 45
    mov [eax + 4], dl
    add ebx, 2Ah
    mov [eax + 5], dl
    add ebx, 'A'
    mov [eax + 6], dl
    add ebx, 19h
    mov [eax + 7], dl
    add ebx, 77
    mov [eax + 8], dl
    add ebx, 1Ch
    mov [eax + 9], dl
    add ebx, 'Z'
    mov [eax + 10], dl
    add ebx, 88
    mov [eax + 11], dl
    add ebx, 4Eh
    mov [eax + 12], dl
    add ebx, 33
    mov [eax + 13], dl
    add ebx, 12
    xor eax, eax
    lea eax, ascii
    mov [eax], dl
    mov [eax + 1], dl
    add ebx, 'H'
    mov [eax + 2], dl
    add ebx, 3Fh
    mov [eax + 3], dl
    add ebx, 45
    mov [eax + 4], dl
    add ebx, 2Ah
    mov [eax + 5], dl
    add ebx, 'A'
    mov [eax + 6], dl
    add ebx, 19h
    mov [eax + 7], dl
    add ebx, 77
    mov [eax + 8], dl
    add ebx, 1Ch
    mov [eax + 9], dl
    add ebx, 'Z'
    mov [eax + 10], dl
    add ebx, 88
    mov [eax + 11], dl
    add ebx, 4Eh
    mov [eax + 12], dl
    add ebx, 33
    mov [eax + 13], dl
    add ebx, 5Dh
    mov [eax + 14], dl
    add ebx, 27
    mov [eax + 15], dl
    add ebx, 6Ch
    mov [eax + 16], dl
    add ebx, 9
    mov [eax + 17], dl
    add ebx, 'M'
    mov [eax + 18], dl
    add ebx, 3Ah
    mov [eax + 19], dl
    add ebx, 51
    mov [eax + 20], dl
    add ebx, 78h
    mov [eax + 21], dl