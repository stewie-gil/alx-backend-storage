-- creates index for the first letter and score
CREATE INDEX idx_name_first_score ON names (name(1), score);
