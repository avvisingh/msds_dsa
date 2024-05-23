#Coding Solutions for binary search here
import random as r

#non-recursive attempt
def nrec_binary_search(arr, elt):
    # print(f"This is outside the for loop")
    left = 0
    right = len(arr) - 1
    # print(f"left: {left}")
    # print(f"right: {right}")

    # print('Now entering the while loop')
    i = 1
    while left <= right:
        # print('##### ##### ##### ##### ##### #####')
        # print(f'This is iteration {i} of the while loop')
        # print(f'left: {left}')
        # print(f'right: {right}')
        mid = (left+right)//2
        # print(f'mid: {mid}')
        curr = arr[mid]
        # print(f'current element being inspected: {curr}')
        if curr == elt:
            # print(f'Element ({elt}) has been found at index: {mid}')
            return mid
        elif elt < curr:
            right = mid - 1
            i+=1
            # print(f'Element ({elt}) is smaller than curr ({curr}). right pointer is now: {right}')
        else:
            left = mid + 1
            i+=1
            # print(f'Element ({elt}) is larger than curr ({curr}). left pointer is now: {left}')

    # print(f'last index checked was {mid} and {elt} was not found.')
    return None

test_inputs = [["Set 48", -291, -287, -278, -260, -249, -208, -187, -184, -178, -171, -170, -151, -142, -132, -115, -109, -99, -77, -69, -61, -56, -52, -45, -41, -31, -9, 0, 30, 54, 63, 95, 106, 109, 120, 136, 137, 156, 176, 191, 200, 201, 217, 227, 256, 261, 271, 276, 287, 296, 297],
["Set 8", -296, -288, -268, -260, -231, -194, -133, -127, -120, -119, -115, -97, -95, -90, -86, -85, -82, -79, -68, -66, -52, -44, -6, -2, 2, 12, 28, 33, 52, 55, 73, 89, 101, 127, 169, 170, 176, 183, 189, 200, 202, 215, 238, 250, 266, 274, 281, 282, 286, 293],
["Set 50", -287, -286, -270, -267, -264, -218, -201, -200, -196, -181, -174, -169, -166, -163, -155, -154, -153, -151, -130, -123, -120, -95, -66, -62, -29, -27, -26, -16, -9, 22, 23, 33, 45, 48, 84, 114, 125, 129, 137, 138, 148, 150, 151, 153, 159, 169, 174, 262, 269, 285],
["Set 24", -284, -270, -254, -230, -210, -167, -157, -149, -142, -129, -124, -120, -117, -111, -92, -87, -73, -69, -55, -48, -36, -25, -12, -1, 4, 19, 33, 45, 67, 85, 86, 89, 110, 112, 134, 145, 153, 154, 164, 180, 184, 193, 210, 212, 216, 219, 237, 262, 275, 294],
["Set 38", -298, -287, -272, -268, -255, -249, -244, -220, -212, -196, -167, -166, -146, -119, -114, -108, -102, -94, -93, -86, -85, -56, -55, -54, -43, -40, -16, 0, 12, 13, 19, 32, 41, 46, 53, 62, 99, 131, 136, 138, 147, 153, 154, 190, 231, 234, 250, 252, 258, 293],
["Set 22", -295, -261, -258, -257, -246, -243, -235, -229, -228, -226, -214, -198, -189, -174, -154, -143, -134, -132, -125, -111, -110, -104, -97, -87, -80, -72, -52, -42, -27, -14, 16, 17, 76, 86, 91, 100, 115, 138, 150, 185, 206, 213, 217, 232, 241, 242, 245, 256, 260, 270],
["Set 19", -290, -241, -219, -213, -204, -197, -183, -178, -177, -170, -161, -144, -136, -115, -112, -104, -96, -91, -80, -43, -37, -4, 31, 43, 45, 54, 58, 62, 66, 75, 83, 111, 113, 120, 145, 148, 154, 157, 174, 190, 198, 218, 221, 234, 251, 267, 278, 285, 286, 292],
["Set 14", -277, -261, -259, -257, -243, -234, -229, -190, -188, -182, -162, -123, -114, -95, -92, -75, -74, -46, -40, -37, 23, 25, 40, 49, 74, 83, 84, 92, 102, 117, 147, 151, 152, 174, 181, 182, 210, 228, 239, 240, 241, 243, 247, 256, 257, 260, 268, 272, 276, 278],
["Set 34", -277, -274, -273, -256, -247, -244, -238, -232, -213, -205, -203, -185, -184, -176, -172, -132, -128, -107, -91, -90, -69, -20, -17, -11, 18, 20, 24, 27, 30, 31, 40, 41, 45, 46, 55, 77, 108, 124, 151, 154, 162, 188, 198, 223, 225, 256, 277, 290, 291, 293],
["Set 47", -292, -289, -253, -246, -244, -230, -227, -219, -217, -208, -181, -179, -178, -154, -152, -142, -140, -20, -2, 1, 8, 19, 40, 56, 71, 76, 78, 100, 107, 124, 126, 135, 143, 147, 152, 157, 182, 184, 185, 218, 222, 233, 250, 255, 256, 263, 269, 271, 273, 294],
["Set 44", -282, -280, -272, -267, -260, -246, -235, -230, -205, -196, -188, -181, -171, -152, -124, -122, -108, -97, -93, -91, -87, -74, -47, -43, -42, -36, -21, -10, -6, 9, 20, 28, 41, 49, 57, 70, 93, 157, 160, 170, 186, 195, 200, 224, 240, 246, 255, 265, 291, 296],
["Set 29", -298, -288, -282, -255, -241, -225, -222, -196, -189, -172, -164, -140, -138, -133, -123, -100, -98, -80, -73, -59, -42, -35, -30, -18, -8, 5, 16, 24, 34, 40, 48, 81, 106, 108, 115, 122, 126, 133, 154, 160, 181, 215, 227, 230, 233, 237, 250, 255, 286, 292],
["Set 11", -274, -251, -248, -246, -229, -221, -187, -174, -156, -153, -151, -140, -129, -116, -109, -92, -87, -83, -56, -49, -32, -24, -22, -17, -8, 0, 8, 15, 16, 36, 55, 66, 79, 106, 116, 122, 124, 131, 135, 137, 138, 139, 146, 153, 185, 199, 221, 249, 280, 281],
["Set 20", -295, -293, -284, -276, -271, -261, -242, -202, -180, -167, -163, -160, -158, -157, -145, -137, -131, -128, -104, -58, -53, -42, -34, -7, -4, -3, 16, 18, 55, 62, 75, 83, 97, 133, 144, 146, 150, 157, 194, 195, 216, 246, 263, 266, 274, 280, 284, 288, 290, 294],
["Set 6", -294, -286, -281, -272, -269, -264, -263, -260, -242, -230, -222, -220, -209, -198, -172, -167, -157, -124, -5, 15, 21, 27, 30, 34, 36, 60, 75, 76, 77, 78, 87, 92, 100, 108, 117, 126, 131, 132, 134, 144, 152, 156, 166, 179, 213, 214, 224, 270, 278, 297],
["Set 30", -299, -263, -260, -233, -222, -205, -200, -195, -172, -153, -145, -144, -129, -108, -90, -62, -43, -41, -38, -36, -7, 10, 21, 45, 80, 85, 96, 97, 108, 110, 111, 117, 121, 148, 149, 154, 168, 172, 179, 182, 195, 200, 203, 209, 241, 246, 257, 263, 273, 298],
["Set 31", -299, -295, -254, -226, -223, -220, -214, -189, -164, -140, -135, -123, -113, -109, -105, -69, -58, -51, -23, 2, 5, 14, 15, 26, 37, 38, 44, 46, 60, 64, 70, 71, 86, 91, 104, 106, 109, 116, 118, 129, 143, 171, 181, 198, 201, 203, 229, 276, 279, 284],
["Set 10", -295, -282, -279, -278, -271, -270, -260, -246, -239, -226, -217, -192, -189, -180, -155, -143, -140, -137, -121, -70, -33, -31, -5, 9, 22, 28, 31, 35, 44, 69, 72, 75, 76, 92, 106, 107, 109, 111, 139, 175, 178, 188, 197, 220, 223, 251, 264, 268, 272, 278],
["Set 42", -299, -265, -248, -238, -229, -225, -219, -209, -195, -190, -180, -179, -146, -142, -120, -116, -98, -95, -91, -84, -57, -51, -43, -38, -26, -23, -3, -2, -1, 0, 1, 4, 27, 39, 44, 62, 77, 78, 82, 101, 115, 131, 136, 200, 212, 230, 275, 283, 285, 293],
["Set 4", -276, -275, -253, -210, -192, -175, -174, -173, -171, -165, -160, -145, -139, -131, -92, -86, -71, -49, -34, -8, 15, 17, 21, 30, 55, 71, 75, 83, 93, 113, 120, 135, 144, 166, 168, 171, 179, 204, 224, 237, 245, 248, 256, 259, 262, 266, 277, 280, 285, 300],
["Set 41", -294, -291, -286, -277, -265, -261, -236, -222, -220, -204, -187, -174, -164, -162, -155, -150, -130, -114, -112, -107, -81, -80, -68, -62, -59, -47, -41, -39, -30, -26, -9, 7, 23, 25, 64, 69, 90, 120, 139, 151, 163, 169, 181, 199, 200, 201, 285, 286, 294, 295],
["Set 23", -294, -289, -275, -273, -267, -266, -256, -255, -226, -225, -223, -214, -211, -191, -159, -153, -142, -134, -131, -130, -70, -35, -17, 8, 18, 30, 36, 47, 59, 75, 95, 99, 104, 105, 117, 134, 141, 144, 162, 172, 194, 196, 206, 219, 230, 231, 242, 250, 280, 289],
["Set 17", -287, -263, -261, -227, -221, -215, -203, -191, -187, -169, -167, -154, -152, -149, -143, -142, -136, -133, -116, -114, -111, -105, -102, -83, -68, -57, -47, 13, 38, 45, 83, 88, 101, 108, 143, 144, 171, 174, 192, 196, 199, 218, 222, 245, 246, 250, 262, 288, 291, 293],
["Set 21", -299, -298, -295, -285, -277, -255, -207, -171, -134, -133, -132, -122, -87, -73, -60, -59, -54, -22, -11, 8, 27, 61, 64, 69, 73, 95, 100, 101, 111, 118, 130, 142, 157, 160, 171, 177, 178, 210, 212, 224, 225, 227, 228, 244, 247, 249, 257, 274, 282, 295],
["Set 18", -297, -272, -269, -257, -253, -247, -242, -240, -227, -226, -217, -195, -167, -155, -153, -149, -142, -137, -133, -116, -112, -99, -76, -67, -38, -37, -31, -14, -7, 5, 8, 12, 41, 52, 82, 90, 106, 141, 148, 162, 172, 206, 209, 227, 235, 236, 245, 258, 276, 277],
["Set 12", -298, -290, -284, -280, -266, -221, -192, -179, -170, -167, -162, -148, -131, -130, -127, -109, -95, -90, -51, -37, -14, -3, 1, 11, 23, 45, 59, 61, 62, 63, 68, 95, 97, 105, 129, 139, 158, 177, 218, 219, 240, 263, 265, 268, 269, 270, 273, 279, 287, 297],
["Set 46", -293, -291, -285, -283, -261, -248, -242, -229, -227, -200, -175, -174, -147, -142, -141, -136, -125, -120, -109, -93, -87, -74, -61, -50, -36, -25, -24, -9, 15, 24, 64, 105, 128, 162, 166, 180, 202, 211, 215, 225, 231, 238, 239, 246, 253, 260, 262, 281, 290, 298],
["Set 45", -297, -296, -287, -271, -269, -233, -219, -199, -178, -171, -154, -133, -117, -88, -78, -73, -66, -62, -54, -23, -20, -14, -7, 15, 29, 32, 59, 68, 72, 74, 75, 88, 90, 105, 108, 117, 128, 144, 147, 153, 161, 168, 169, 188, 226, 250, 256, 272, 273, 280],
["Set 15", -281, -277, -274, -262, -240, -233, -221, -219, -218, -196, -195, -191, -169, -160, -117, -106, -80, -55, -29, -27, -25, -17, -5, 13, 15, 32, 37, 43, 60, 76, 85, 94, 95, 124, 142, 162, 164, 175, 212, 214, 218, 238, 240, 244, 246, 248, 256, 264, 267, 270],
["Set 27", -286, -279, -250, -227, -213, -205, -188, -185, -164, -155, -136, -89, -82, -78, -75, -71, -67, -57, -51, -31, -23, -16, -14, -12, 6, 43, 50, 63, 69, 91, 96, 106, 109, 136, 165, 166, 167, 170, 172, 176, 181, 183, 184, 197, 199, 212, 227, 240, 278, 282],
["Set 2", -276, -259, -252, -249, -221, -210, -204, -203, -191, -173, -158, -156, -155, -154, -153, -152, -108, -103, -101, -94, -80, -74, -66, -52, -51, -36, -32, -10, 17, 79, 99, 117, 120, 126, 129, 138, 139, 148, 159, 165, 171, 172, 189, 231, 257, 261, 263, 264, 282, 286],
["Set 26", -297, -293, -291, -268, -262, -258, -222, -221, -201, -200, -194, -188, -184, -173, -149, -148, -145, -144, -142, -130, -125, -119, -115, -109, -107, -70, -56, -54, -43, -10, -3, 12, 22, 36, 42, 63, 66, 71, 108, 127, 129, 130, 198, 201, 210, 222, 225, 229, 255, 258],
["Set 49", -274, -260, -244, -230, -220, -219, -209, -188, -172, -170, -169, -135, -129, -122, -117, -91, -67, -57, -44, -20, -10, -7, 2, 29, 48, 59, 70, 75, 94, 99, 105, 110, 125, 126, 136, 152, 165, 176, 189, 199, 220, 226, 232, 236, 245, 246, 255, 278, 283, 293],
["Set 7", -279, -275, -244, -237, -234, -218, -194, -187, -178, -171, -147, -132, -119, -107, -105, -59, -56, -53, -7, -3, 15, 18, 36, 48, 54, 58, 77, 78, 90, 96, 103, 121, 122, 123, 137, 152, 166, 172, 177, 193, 195, 207, 229, 233, 236, 247, 268, 284, 295, 298],
["Set 33", -289, -284, -283, -266, -261, -245, -238, -228, -189, -188, -175, -166, -142, -137, -131, -119, -115, -102, -91, -90, -88, -85, -74, -70, -30, -17, 23, 27, 54, 60, 61, 71, 83, 96, 100, 102, 110, 124, 138, 151, 152, 169, 204, 211, 232, 235, 277, 286, 288, 296],
["Set 13", -277, -251, -243, -240, -235, -200, -162, -151, -125, -122, -117, -103, -88, -87, -86, -85, -49, -48, -36, -33, -7, 28, 63, 67, 73, 76, 95, 101, 102, 104, 105, 117, 137, 141, 143, 150, 158, 165, 170, 174, 177, 190, 197, 211, 228, 231, 248, 250, 256, 276],
["Set 43", -298, -295, -273, -267, -265, -255, -252, -242, -238, -231, -228, -224, -221, -218, -213, -210, -188, -149, -143, -138, -120, -108, -101, -69, -68, -65, -61, -58, -18, 9, 25, 34, 39, 57, 63, 69, 85, 142, 161, 179, 195, 207, 208, 212, 224, 243, 256, 267, 277, 297],
["Set 35", -299, -293, -270, -239, -235, -233, -224, -207, -195, -192, -190, -180, -167, -146, -143, -139, -105, -101, -87, -84, -80, -74, -60, -42, -34, -17, -11, 18, 47, 84, 110, 124, 127, 130, 146, 175, 183, 185, 187, 192, 215, 218, 227, 237, 250, 259, 266, 280, 291, 298],
["Set 36", -295, -283, -255, -254, -251, -245, -244, -241, -225, -223, -220, -196, -195, -182, -171, -164, -130, -129, -115, -71, -67, -38, -30, -24, -13, 5, 22, 53, 56, 76, 83, 96, 98, 120, 135, 138, 141, 145, 153, 162, 174, 195, 248, 250, 255, 256, 262, 279, 292, 296],
["Set 37", -293, -292, -287, -280, -275, -266, -249, -204, -203, -201, -187, -178, -157, -136, -128, -114, -85, -77, -73, -53, -48, -47, -22, -20, -3, 2, 29, 33, 38, 75, 79, 94, 114, 125, 129, 131, 158, 165, 172, 199, 211, 218, 219, 224, 233, 264, 270, 276, 279, 285],
["Set 16", -269, -254, -250, -244, -243, -234, -233, -202, -199, -193, -184, -182, -181, -164, -155, -138, -134, -125, -88, -67, -50, -36, -35, -9, -7, -5, -4, 4, 8, 9, 13, 17, 80, 89, 99, 101, 104, 108, 126, 134, 135, 149, 156, 182, 209, 223, 232, 272, 286, 299],
["Set 1", -266, -239, -217, -211, -206, -205, -159, -142, -132, -125, -116, -105, -99, -79, -63, -46, -25, -20, -16, -15, -10, 19, 21, 26, 33, 46, 59, 61, 69, 96, 107, 140, 157, 159, 177, 180, 186, 187, 190, 194, 201, 207, 211, 233, 246, 266, 279, 284, 288, 292],
["Set 39", -294, -291, -279, -264, -262, -261, -259, -256, -250, -226, -224, -213, -193, -153, -152, -146, -145, -132, -111, -83, -76, -54, -45, -42, -30, 16, 29, 39, 57, 61, 64, 74, 79, 84, 106, 117, 119, 121, 151, 153, 185, 188, 206, 224, 244, 248, 256, 260, 270, 275],
["Set 28", -281, -278, -267, -257, -245, -230, -207, -199, -184, -174, -163, -162, -160, -155, -153, -148, -129, -124, -117, -107, -94, -69, -59, -51, -42, -27, -19, -6, 2, 17, 23, 30, 37, 69, 105, 121, 130, 131, 141, 143, 145, 153, 158, 170, 190, 202, 211, 228, 234, 293],
["Set 32", -264, -255, -233, -230, -212, -200, -193, -180, -169, -161, -137, -130, -128, -86, -73, -68, -67, -61, -56, -45, -31, -30, -21, 33, 41, 49, 52, 54, 75, 84, 90, 97, 113, 115, 133, 141, 199, 203, 216, 220, 225, 229, 242, 252, 254, 268, 275, 286, 290, 300],
["Set 25", -280, -267, -243, -232, -210, -186, -185, -166, -163, -146, -143, -142, -134, -127, -124, -87, -84, -66, -34, -19, -15, -6, 5, 32, 35, 40, 46, 70, 74, 91, 106, 109, 123, 127, 137, 139, 159, 163, 166, 170, 181, 190, 193, 231, 241, 248, 279, 282, 288, 291],
["Set 5", -299, -284, -274, -248, -231, -219, -216, -209, -207, -202, -192, -182, -176, -168, -147, -136, -128, -126, -119, -114, -110, -107, -100, -61, -54, -53, -36, -7, -1, 21, 48, 54, 55, 71, 110, 116, 117, 119, 124, 141, 175, 193, 220, 233, 235, 249, 260, 269, 286, 295],
["Set 40", -298, -270, -259, -247, -231, -206, -199, -195, -183, -182, -176, -169, -132, -122, -112, -104, -95, -89, -84, -74, -25, -21, -9, 4, 15, 18, 37, 44, 62, 93, 96, 110, 119, 135, 156, 157, 159, 163, 184, 189, 190, 200, 211, 219, 223, 229, 240, 256, 275, 293],
["Set 3", -288, -285, -272, -266, -259, -225, -210, -192, -181, -159, -153, -132, -124, -109, -105, -98, -64, -34, -24, -5, -1, 20, 23, 27, 29, 44, 45, 49, 52, 53, 61, 64, 78, 92, 105, 120, 121, 135, 138, 143, 199, 210, 224, 225, 232, 247, 253, 262, 270, 278],
["Set 9", -286, -276, -263, -254, -235, -232, -222, -210, -182, -181, -151, -135, -130, -121, -119, -113, -103, -99, -67, -65, -51, -46, -21, -12, -8, -6, 38, 42, 50, 55, 72, 74, 77, 109, 117, 132, 134, 136, 148, 154, 170, 174, 177, 181, 196, 207, 252, 266, 268, 271]]


results = []
incorrect_ans = []
for arr in test_inputs:
    curr_arr = arr[0]
    test_arr = arr[1:len(arr)]
    curr_res = {}
    curr_res['set'] = curr_arr

    elt_1 = r.randint(-299,300)
    elt_2 = r.randint(-299,300)
    elt_3 = r.randint(-299,300)
    elt_4 = r.randint(-499,-300)
    elt_5 = r.randint(301,400)
    test_elts = [elt_1, elt_2, elt_3, elt_4, elt_5]

    for elt in test_elts:
        try:
            ans = test_arr.index(elt)
        except:
            ans = None
        
        my_ans = nrec_binary_search(test_arr, elt)

        if my_ans == ans:
            result = 'correct'
        else:
            result = 'wrong'
            incorrect_ans.append([curr_arr, elt, result])
        
        curr_res[elt] = [ans, my_ans, result]
    
    results.append(curr_res)
    print('finished')

for i in incorrect_ans:
    print(f"{i}\n")

for res in results:
    for k, v in res.items():
        print(f'{k}: {v}')

# 29 was not found in ["Set 6", -28, -23, -21, -15, -14, -9, -7, -5, -3, 2, 3, 4, 9, 10, 14, 17, 20, 23, 26, 29]
#Debugging

# nrec_binary_search([-28, -23, -21, -15, -14, -9, -7, -5, -3, 2, 3, 4, 9, 10, 14, 17, 20, 23, 26, 29], 29)