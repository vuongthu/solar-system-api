from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    has_moon = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            has_moon=self.has_moon,
        )

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            description=data_dict["description"],
            has_moon=data_dict["has_moon"]
        )

    def replace_details(self, data_dict):
        self.name = data_dict["name"]
        self.description = data_dict["description"]
        self.has_moon = data_dict["has_moon"]

    def check_keys(self, data_dict):

        patch_keys = data_dict.keys()
        for key in ["name", "description", "has_moon"]:
            if key in patch_keys:
                setattr(self, key, data_dict[key])