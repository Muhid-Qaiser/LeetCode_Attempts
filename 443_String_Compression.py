class Solution:
    def compress(self, chars: List[str]) -> int:

        read, write, count, n = 0, 0, 0, len(chars)

        while read < n:
            curr = chars[read]
            read += 1
            count = 1

            while read < n and chars[read] == curr:
                read += 1
                count += 1

            chars[write] = curr
            write += 1

            if count > 1:
                count = str(count)
                for i in list(count):
                    chars[write] = i
                    write += 1

        return write

        