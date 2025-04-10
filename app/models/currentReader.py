class currentReader:
    id = None
    role = None  # 1 = user, 2 = writer, 3 = admin

    @staticmethod
    def set(reader_id, role):
        currentReader.id = reader_id
        currentReader.role = role

    @staticmethod
    def get_id():
        return currentReader.id

    @staticmethod
    def get_role():
        return currentReader.role