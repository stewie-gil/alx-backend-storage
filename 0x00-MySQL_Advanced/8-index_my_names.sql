-- indexing the first later of the name column on names table
CREATE INDEX indx_name_first ON names(name(1));
