# Python 3 program for the above approach

# Stores the X and Y coordinate of
# a point respectively
# define pdd pair<double, double>

# Function to find the line given
# two points
def lineFromPoints(P, Q, a, b, c):
    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a * (P[0]) + b * (P[1])

# Function to convert the input line
# to its perpendicular bisector


def perpendicularBisector(P, Q, a, b, c):
    mid_point = [(P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2]

    # c = -bx + ay
    c = -b * (mid_point[0]) + a * (mid_point[1])
    temp = a
    a = -b
    b = temp

# Function to find the
# intersection point of two lines


def lineLineIntersection(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    # As points are non-collinear,
    # determinant cannot be 0
    if determinant != 0:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
    else:
        x = (b2 * c1 - b1 * c2)
        y = (a1 * c2 - a2 * c1)

    return [x, y]

# Function to find the
# circumcenter of a triangle


def findCircumCenter(A):
    P = A[0]
    Q = A[1]
    R = A[2]

    # Line PQ is represented as
    # ax + by = c
    a = 0
    b = 0
    c = 0
    lineFromPoints(P, Q, a, b, c)

    # Line QR is represented as
    # ex + fy = g
    e = 0
    f = 0
    g = 0
    lineFromPoints(Q, R, e, f, g)

    # Converting lines PQ and QR
    # to perpendicular bisectors
    perpendicularBisector(P, Q, a, b, c)
    perpendicularBisector(Q, R, e, f, g)

    # Their point of intersection
    # gives the circumcenter
    circumcenter = lineLineIntersection(a, b, c, e, f, g)

    # Return the circumcenter
    return circumcenter

# Function to find the
# centroid of a triangle


def findCentroid(A):

    # Centroid of a triangle is
    # given as (Xa + Xb + Xc)/3,
    # (Ya + Yb + Yc)/3
    centroid = [(A[0][0] + A[1][0] + A[2][0]) / 3,
                (A[0][1] + A[1][1] + A[2][1])/3]

    # Return the centroid
    return centroid

# Function to find the
# orthocenter of a triangle


def findOrthocenter(A):

    # Store the circumcenter and
    # the centroid of triangle
    circumcenter = findCircumCenter(A)
    centroid = findCentroid(A)

    # Apply External section formula:
    # (mX1 - nX2)/(m - n), (mY1 - nY2)/(m - n)
    h = [(3 * centroid[0] - 2 * circumcenter[0]),
         (3 * centroid[1] - 2 * circumcenter[1])]

    # Print the x and y-coordinate
    h[0] = h[0] - 0.400

    # of the orthocenter of the triangle
    print("(", "{:.3f}".format(h[0]), ",", "{:.3f}".format(-h[1]), ")")


# Driver Code
if __name__ == '__main__':

    # Given points P, Q, R
    A = [[-3, 1], [2, 2], [-3, -5]]
    findOrthocenter(A)

    # This code is contributed by rathorenav123.
